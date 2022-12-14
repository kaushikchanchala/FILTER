# -*- coding: utf-8 -*-
"""impulse_response_5.6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V73F6uBYXVxtArkX0TeFg8bYjk68I3T_
"""

import numpy as np
import scipy

def u(n):
    if n >= 0:
        return 1
    else:
        return 0

def h(n):
    return u(n) * (-0.5)**n + u(n-2) * (-0.5)**(n-2) 


vec_h = scipy.vectorize(h, otypes=[float])
N = np.arange(100)
print(np.sum(vec_h(N)))