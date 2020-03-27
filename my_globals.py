import math

class G:  
    max_time=1200
    rupture_prob=0.2
    sex_prob=0.5
    
def moaning_periods(age):
    if age<15:
        return 1/3
    if 15<=age<35:
        return 1/6
    if 35<=age<45:
        return 1/12
    if 45<=age<60:
        return 1/24
    if 60<=age:
        return 1/48
    
def desire_probs(age):
    if 12<=age<15:
        return 0.6
    if 15<=age<21:
        return 0.65
    if 21<=age<35:
        return 0.8
    if 35<=age<45:
        return 0.6
    if 45<=age<60:
        return 0.5
    if 60<=age<125:
        return 0.2
    return 0
    
def pregnancy_probs(age):
    if 12<=age<15:
        return 0.2
    if 15<=age<21:
        return 0.85
    if 21<=age<25:
        return 0.9
    if 25<=age<30:
        return 0.8
    if 30<=age<35:
        return 0.75
    if 35<=age<40:
        return 0.55
    if 40<=age<45:
        return 0.38
    if 45<=age<=60:
        return 0.05
    return 0
    
def death_probs(age, sex):
    if age<=1:
        return 1/(136*12) if sex=='M' else 1/(193*12)
    if 1<age<=4:
        return 1/(4386*12) if sex=='M' else 1/(5376*12)
    if 4<age<=14:
        return 1/(8333*12) if sex=='M' else 1/(10417*12)
    if 14<age<=24:
        return 1/(1908*12) if sex=='M' else 1/(4132*12)
    if 24<age<=34:
        return 1/(1215*12) if sex=='M' else 1/(2488*12)
    if 34<age<=44:
        return 1/(663*12) if sex=='M' else 1/(1106*12)
    if 44<age<=54:
        return 1/(279*12) if sex=='M' else 1/(421*12)
    if 54<age<=64:
        return 1/(112*12) if sex=='M' else 1/(178*12)
    if 64<age<=74:
        return 1/(42*12) if sex=='M' else 1/(65*12)
    if 74<age<=84:
        return 1/(15*12) if sex=='M' else 1/(21*12)
    return 1/(6*12) if sex=='M' else 1/(7*12)
       
    
def getting_together_probs(dif):
    if dif<5:
        return 0.45
    if 5<=dif<10:
        return 0.4 
    if 10<=dif<15:
        return 0.35 
    if 15<=dif<20:
        return 0.25
    if dif>=20:
        return 0.15 
     
def multiple_born_prob(u):
    if u < 0.01:
        return 2
    if u < 0.011:
        return 3
    if u < 0.0111:
        return 4
    return 1

def how_many_children(u):
    if u < 0.001:
        return 0
    if u < 0.551:
        return 1
    if u < 0.951:
        return 2
    if u < 0.99:
        return 3
    if u < 0.991:
        return 4
    if u < 0.9911:
        return 5
    return math.inf
            
    
    