import math
import random as rnd

def __elem_sum__(l1, l2):
    if len(l1)!=len(l2):
        raise Exception()
    lr=[]
    for i in range(len(l1)):
        lr.append(l1[i]+l2[i])
    return lr

def __exponential__(_lambda):
    return math.log(rnd.uniform(0,1))/(-_lambda)


def __oposite__(sex):
    if sex=='F':
        return 'M'
    return 'F'