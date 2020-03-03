import math
import numpy as np
from operator import itemgetter


def cohen_d_effect_size(g1, g2):
    '''
    d = (x-bar1 - x-bar2) / s
    g1,g2 Series or numpy array
    '''
    v1, v2 = g1.var(), g2.var()
    n1, n2 = len(g1), len(g2)
    pooled_var = ((n1*v1) + (n2*v2)) / n1+n2
    return (g1.mean() - g2.mean()) / math.sqrt(pooled_var)


# np.random.seed(42)
one = np.random.randn(100)
two = np.random.randn(100)
d = cohen_d_effect_size(one, two)
print("effect size of two normal distributions: ", d)

# [print(cohen_d_effect_size(np.random.randn(100), np.random.randn(100))) for _ in range(100)]
res = [x < 0.5 for x in [cohen_d_effect_size(np.random.randn(100), np.random.randn(100)) for _ in range(100)]]
# print(res)
un = np.unique(res)
print("effect size test all same value: ", len(un) == 1)
print("effect size test for all values meeting condition 'x<0.5' == : ", un[0] == True)


def find_mode(hist):
    '''
    hist is a histogram map of value:count pairs
    {1:3,2:4,3:6}
    '''
    return max([(v, k) for k, v in hist.Items()])[0]


def find_all_modes(hist):
    return sorted(hist.Items, key=itemgetter(1), reverse=True)
