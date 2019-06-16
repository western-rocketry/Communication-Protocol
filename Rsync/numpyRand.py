from inspect import getsourcefile
from os.path import dirname, abspath
"""
Created on Thu Mar 14 15:35:19 2019

@author: Garvan
"""
parentDir = dirname(abspath(getsourcefile(lambda:0)))
import numpy as np
for i in 15000:
    random = np.random.randint(0,16,(4,4))
    np.save(parentDir + "/" + i, random)
    

    
