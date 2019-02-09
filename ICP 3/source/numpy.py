# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:33:25 2019

@author: saidivya
"""

import numpy as np
x = np.random.randint(0, 20, 15)
print(x)
print("Most frequent value in the above array:")
a=np.bincount(x)
print(a.argmax())