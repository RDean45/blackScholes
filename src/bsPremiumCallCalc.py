import requests as rq
import pandas as ps
import numpy
import math
from scipy import stats
from scipy.stats import norm

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
    d1Value = d1(s,k,T,stdDev,rfr)
    d2Value = d2(d1Value,stdDev,T)
    callPremium = (norm.cdf(d1Value)*s)-norm.cdf(d2Value)*k*math.exp(-rfr*T)
    return callPremium