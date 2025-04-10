import requests as rq
import math
from scipy import stats
from scipy.stats import norm
import bsPremiumCallCalc as callPremiumCalc
import bsStdDevCallCalc as stdDevCalc
import theta as theta
import gamma as gam
import vega
import delta
import rho

def main(option):
    type = 'c'
    s = 43.72
    k = 50
    T = .4
    rfr = .04
    stdDev = .43
    var = False
    if var:
        stddev = math.sqrt(var)
        print(f'Hidden StdDev: {stddev}')
    elif stdDev:
        var = stdDev ** 2
        print(f'Hidden Variance: {var}')
    premium = 37.89026557896523
    #varGuess = stdDevCalc.computeStdDevCall(s,k,T,rfr,premium,var)
    #print(f'Var: {varGuess}')
    #gamma = gam.gamma(s,k,T,stdDev,rfr)
    #print(f'Gamma: {gamma}')
    #callPremium = callPremiumCalc.blackScholesCall(s,k,T,var,rfr)
    #print(callPremium)


#optionDetails = {'type':None,'s': 0,'k':0,'t':0,'rfr': 0,'var': 0,'premium':0}

main()

#things we need to implement
#1. the rest of the greeks
#2. inputs (last)
#3. pull info from the web to auto update, like rfr, current premium, etc
#4.