'''
confidence_interval.py: Script to figure out the confidence intervals for the mean value of a certain measure 
Assumption is that we do not know the mean of the certain measure, but we have some measurements pertaining to that measure
Here, we will learn about the confidence intervals in cases where the underlying distribution is a t-distribution and also in the case where the underlying distribution is a normal distribution
Author: Abhirup gupta
'''

import numpy as np
from scipy import stats
from scipy.stats import t
from typing import Tuple

def confidence_interval_t(x: np.array, conf: float = 0.95) -> Tuple[np.float64, np.float64]:
    """
    get confidence interval considering that the underlying distribution from which the numbers have been sampled is a t-distribution
    We need to use a t-distribution when the sample size is very low (< 30)
    If the sample size > 30, then we can assume that the distribution of the mean would be a normal distribution ( Central limit theorem)
    Args:
        x (np.array):  Input array containing the list of observations in the sample
        conf (float): This is the confidence interval that we should consider ( e.g. 95%, 90% ) ( 95 % by default)

    Returns:
        Tuple[np.float64, np.float64]:  Returns the lower limit and the upper limit of the confidence interval
    """
    m  = x.mean()   
    std = x.std()

    dof = len(x) - 1  # this is the degrees of freedom

    t_crit = np.abs(t.ppf((1 - conf)/2, dof))

    lower_limit = m - (std * t_crit)/np.sqrt(len(x))
    upper_limit = m + (std * t_crit)/np.sqrt(len(x))

    return lower_limit, upper_limit

def confidence_interval_normal(x: np.array, conf: float = 0.95) -> Tuple[np.float64, np.float64]:
    """
    get the confidence interval assuming that the sample size is greater than 30, and the observations have been sampled from an underlying normal distribution

    Args:
        x (n.array): Input array containing the observations in the sample
        conf (float, optional): This is the confidence interval. Defaults to 0.95.

    Returns:
        Tuple[np.float64, np.float64]: Lower limit and upper limit of the confidence interval
    """
    m = x.mean()
    std = x.std()
    ci = stats.norm.interval(conf, loc= m, scale = std)
    return ci

if __name__ == '__main__':
    # simulating a data set made up of 100 numbers
    x = np.random.normal(size = 100)

    a_t,b_t = confidence_interval_t(x, conf =0.95)
    a_n,b_n = confidence_interval_normal(x, conf=0.95)

    print("Considering that the underlying distribution is a t-distribution, the 95% confidence interval is ", end = "")
    print(a_t, b_t)
    print("Considering that the underlying distribution is a normal-distribution, the 95% confidence interval is ", end = "")
    print(a_n, b_n)

    # we now test two observations regarding the t-distribution
    y = np.random.normal(size = 100)
    a_t1, b_t1 = confidence_interval_t(y)
    interval_1 = b_t1 - a_t1
    y = np.random.normal(size = 10000)
    a_t1, b_t1 = confidence_interval_t(y)
    interval_2 = b_t1 - a_t1

    assert (interval_2 > interval_1)  == False  
    # Observation 1: As the number of points in the sample increases, the approximation becomes more accurate, since the interval length decreases ( Law of Large Numbers)

    z = np.random.normal(size = 100)
    a_t1, b_t1 = confidence_interval_t(z,conf = 0.9)
    interval_1 = b_t1 - a_t1
    z = np.random.normal(size = 100)
    a_t1, b_t1 = confidence_interval_t(z, conf = 0.95)
    interval_2 = b_t1 - a_t1

    assert (interval_2 > interval_1) == True
    # Observation 2: If the number of points in the sample remains the same, then if confidence interval increases, then the interval width also increases.