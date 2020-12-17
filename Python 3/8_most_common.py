#!/bin/python3

# This is the worst code i have ever written...

import math
import os
import random
import re
import sys

from collections import OrderedDict

if __name__ == '__main__':
    S = input()

    dicty,maxi,alpha=OrderedDict(),[0,0,0],[S[0],S[0],S[0]]
    for i in S:
        if i in dicty:
            dicty[i]+=1
        else:
            dicty[i]=1
    for i in dicty:
        if dicty[i]>maxi[2]:
            if dicty[i]>maxi[1]:
                if dicty[i]>maxi[0]:
                    maxi[2],maxi[1],maxi[0]=maxi[1],maxi[0],dicty[i]
                    alpha[2],alpha[1],alpha[0]=alpha[1],alpha[0],i
                elif dicty[i]<maxi[0]:
                    maxi[2],maxi[1]=maxi[1],dicty[i]
                    alpha[2],alpha[1]=alpha[1],i
                elif dicty[i]==maxi[0]:
                    if i<alpha[0]:
                        maxi[2],maxi[1],maxi[0]=maxi[1],maxi[0],dicty[i]
                        alpha[2],alpha[1],alpha[0]=alpha[1],alpha[0],i   
                    else:
                        maxi[2],maxi[1]=maxi[1],dicty[i]
                        alpha[2],alpha[1]=alpha[1],i
            elif dicty[i]<maxi[1]:
                maxi[2]=dicty[i]
                alpha[2]=i
            elif dicty[i]==maxi[1]:
                if i<alpha[1]:
                    maxi[2],maxi[1]=maxi[1],dicty[i]
                    alpha[2],alpha[1]=alpha[1],i
                else:
                    maxi[2]=dicty[i]
                    alpha[2]=i
        elif dicty[i]==maxi[2]:
            if i<alpha[2]:
                maxi[2]=dicty[i]
                alpha[2]=i
        for i in range(len(alpha)-1):
            if maxi[i]==maxi[i+1]:
                if alpha[i]>alpha[i+1]:
                    alpha[i],alpha[i+1]=alpha[i+1],alpha[i]
    for i in range(3):
        print(alpha[i],maxi[i])