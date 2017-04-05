# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------
import os

def AddSysPath(new_path):  
    import sys, os
    if not os.path.exists(new_path): return -1  
    new_path = os.path.abspath(new_path)  
    for x in sys.path:  
          x = os.path.abspath(x)
          if new_path in (x, x + os.sep):  
                 return 0  
    sys.path.append(new_path)  
    return 1
if __name__ == '__main__':
    import sys, os
    abspath = os.path.abspath(__file__)
    AddSysPath(os.path.dirname(abspath))
    for x in sys.path: print (x)
