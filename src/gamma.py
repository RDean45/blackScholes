import math
from scipy import stats
from scipy.stats import norm

def d1(s,k,T,stdDev, rfr):
    d1Numerator = (math.log(s/k) + (rfr + ((stdDev ** 2) * 0.5 )) * T)
    d1Denominator = (stdDev*math.sqrt(T))
    d1 = d1Numerator / d1Denominator
    return d1

def gamma(s,k,T,stdDev, rfr):
    d1Val = d1(s,k,T,stdDev, rfr)
    Nd1Val = norm.pdf(d1Val) #n'(d1)
    gamma = (Nd1Val) / (s * stdDev * math.sqrt(T))
    return gamma