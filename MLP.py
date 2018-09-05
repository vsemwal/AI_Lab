# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 09:28:05 2018

@author: Ashish Jha
"""
#Importing Libraries
import numpy as np
import pandas as od
import matplotlib.pyplot as plt
import sklearn 
from math import *

#Implementation of Different Activation function
def hardlim(x,k):
    op=0 if x<k else 1 
    return op
    
def sigmoid(x):
    return 1/(1+exp(-x))

def tanh(x):
    return (exp(x)-exp(-x))/(exp(x)+exp(-x))

def relu(x):
    op=0 if x<0 else x
    return op

def lrelu(x,a):
    op=a*x if x<0 else x

def softmax(z):
    return np.exp(z)/np.sum(np.exp(z))

print(sigmoid(1))
    
    
