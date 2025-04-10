import requests as rq
import pandas as ps
import numpy
import math
from scipy import stats
from scipy.stats import norm

def d1(s,k,T,stdDev, rfr):
    d1Numerator = (math.log(s/k) + (rfr + ((stdDev ** 2) * 0.5 )) * T)
    d1Denominator = (stdDev*math.sqrt(T))
    delta = d1Numerator / d1Denominator
    return delta