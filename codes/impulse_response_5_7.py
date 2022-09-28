# -*- coding: utf-8 -*-
"""impulse_response_5.7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V73F6uBYXVxtArkX0TeFg8bYjk68I3T_
"""

import numpy as np
import matplotlib.pyplot as plt

k = 12
h = np.zeros(k)
h[0] = 1
h[1] = -0.5*h[0]
h[2] = -0.5*h[1] + 1

for n in range(3,k-1):
		h[n] = -0.5*h[n-1]

#subplots
plt.stem(range(0,k),h,use_line_collection = 'True')
plt.title('Impulse Response Definition')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()# minor

plt.show()