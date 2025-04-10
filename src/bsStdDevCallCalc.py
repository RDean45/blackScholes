import math
from scipy import stats
from scipy.stats import norm
import bsPremiumCallCalc as pcc

def d1(s,k,T,stdDev, rfr):
    d1Numerator = (math.log(s/k) + (rfr + ((stdDev ** 2) * 0.5 )) * T)
    d1Denominator = (stdDev*math.sqrt(T))
    d1 = d1Numerator / d1Denominator
    return d1

def d2(d1, stdDev, T):
    d2 = d1 - stdDev * math.sqrt(T)
    return d2


def computeStdDevCall(s,k,T,rfr,correctPremium,varGuess,error = .05,maxAttempts = 500):
    attemptCounter = 0
    low = 0
    high = max(low,varGuess,10000)
    while True:
        varGuess = (low + high) / 2

        stdDev = math.sqrt(varGuess)

        d1Value = d1(s,k,T,stdDev,rfr)

        d2Value = d2(d1Value,stdDev,T)

        callPremium = (norm.cdf(d1Value) * s) - norm.cdf(d2Value) * k * math.exp(-rfr * T)
        diff = callPremium - correctPremium
        if diff < error and diff > 0.0:
            break
        elif diff > error:
            high = varGuess
        else:
            low = varGuess
        attemptCounter += 1
        if attemptCounter == maxAttempts:
            print(f"Max Attempts of: {maxAttempts} reached!")
            break
    return varGuess
