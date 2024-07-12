#!/bin/python3

import math
import os
import random
import re
import sys



if__name__=='__main__':
   n=int(input().strip())
   if(n%2!=0) or (n>=6 and n<=20):
         print("weird")
     else:
         print("not weird")   