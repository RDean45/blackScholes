import requests as rq
import pandas as ps
import numpy
import math
from scipy import stats
from scipy.stats import norm

def main():
    s = 347
    k = 320
    t = .25
    rfr = .02956
    var = .09
    #callPremium = blackScholesCall(s,k,t,var,rfr)
    premium = 37.89026557896523
    varGuess = computeStdDevCall(s,k,t,rfr,premium,var)
    print(varGuess)

def d1(s,k,T,stdDev, rfr):
    d1Numerator = (math.log(s/k) + (rfr + ((stdDev ** 2) * 0.5 )) * T)
    d1Denominator = (stdDev*math.sqrt(T))
    d1 = d1Numerator / d1Denominator
    return d1

def d2(d1, stdDev, T):
    d2 = d1 - stdDev * math.sqrt(T)
    return d2

def blackScholesCall(s,k,T,var,rfr):
    stdDev = math.sqrt(var)
    print(f"Standard Deviation: {stdDev}")

    d1Value = d1(s,k,T,stdDev,rfr)
    print(f'D1 Value: {d1Value}')

    d2Value = d2(d1Value,stdDev,T)
    print(f'D2 Value: {d2Value}')

    callPremium = (norm.cdf(d1Value)*s)-norm.cdf(d2Value)*k*math.exp(-rfr*T)
    print(f'Call Premium: {callPremium}')

    return callPremium

def computeStdDevCall(s,k,T,rfr,correctPremium,varGuess,error = .05,maxAttempts = 500):
    attemptCounter = 0
    low = 0
    high = max(low,varGuess,10000)
    while True:
        varGuess = (low + high) / 2
        print(f"Variance Guess: {varGuess}")
        stdDev = math.sqrt(varGuess)
        print(f"Standard Deviation Guess: {stdDev}")

        d1Value = d1(s,k,T,stdDev,rfr)
        print(f'D1 Value: {d1Value}')

        d2Value = d2(d1Value,stdDev,T)
        print(f'D2 Value: {d2Value}')

        callPremium = (norm.cdf(d1Value) * s) - norm.cdf(d2Value) * k * math.exp(-rfr * T)
        print(f'Call Premium Guess: {callPremium}')
        print(f'Call Premium Actual: {correctPremium}')
        diff = callPremium - correctPremium
        print(f'Premium Difference: {diff}')
        if diff < error and diff > 0.0:
            break
        elif diff > error:
            high = varGuess
            print("Std Dev To BIG!")
        else:
            low = varGuess
            print("Std Dev To SMALL!")
        attemptCounter += 1
        if attemptCounter == maxAttempts:
            print(f"Max Attempts of: {maxAttempts} reached!")
            break
    print(f'VarGuess: {varGuess}')
    return varGuess

main()