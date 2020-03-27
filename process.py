import simpy as Sim
import random as rnd
import math
from my_globals import *
from person import Woman, Man, Couple
import utils

def couple_visit(c, env):   
    c.man.partner=c.woman
    c.woman.partner=c.man
    env.couples[-1]+=1
    c.man.available=False
    c.woman.available=False

def init_month(env):
    env.obs_pop['F'].append(0)
    env.obs_pop['M'].append(0)
    env.borns.append(0)
    env.deaths.append(0)
    env.average_age.append(0)
    try:
        i=env.couples[-1]
    except:
        i=0
    env.couples.append(i)
    
def monitor(env, p): 
    env.obs_pop[p.sex][-1]+=1
    if p.age==0:
        env.borns[-1]+=1
    env.average_age[-1]+=p.age

def rupture_visit(c, env):
    env.couples[-1]-=1    
    c.man.partner=None
    c.woman.partner=None                
    env.process(moan(c.woman, env))
    env.process(moan(c.man, env))  
           

def moan(person, env):
    _time=utils.__exponential__(moaning_periods(person.age/12))
    yield env.timeout(_time)
    person.available=True
             
def rupture_generator(c, env):
    u=rnd.uniform(0, 1)
    if u <= G.rupture_prob:
        rupture_visit(c, env)
            
def death_generator(person, env): 
    p=death_probs(person.age/12, person.sex)
    u=rnd.uniform(0,1)
    if u<=p:
        death_visit(person, env)
        return True
    return False

def death_visit(person, env):
    env.deaths[-1]+=1
    if person.partner:
            env.couples[-1]-=1
            env.process(moan(person.partner, env))        
            person.partner.partner=None
         
def couple_generator(person1, person2, env):  
    if person1.sex=='F':
        woman=person1
        man=person2
    else:
        man=person1
        woman=person2 
    _dif=abs(woman.age/12-man.age/12)   
    p=getting_together_probs(_dif)
    u=rnd.uniform(0,1)
    if u<=p:  
        c= Couple(woman, man)
        couple_visit(c, env)
       
def desire_visit(person, env):
    _age=person.age/12
    p=desire_probs(_age)    
    u=rnd.uniform(0,1)
    return u<=p
    
        
def pregnancy_visit(c, env):  
    c.woman.pregnant=True
    u=rnd.uniform(0,1)
    pregnancy_time = (u<0.05)*7+(u>=0.05)*9 
    yield env.timeout(pregnancy_time)    
    u=rnd.uniform(0,1)
    ch=multiple_born_prob(u)
    c.woman.childs+=ch
    c.man.childs+=ch
    for _ in range(ch):
        u=rnd.uniform(0,1)
        if u<=G.sex_prob:
            env.new_persons.append(Woman(env.idx))
        else:
            env.new_persons.append(Man(env.idx))
        env.idx+=1  
    c.woman.pregnant=False
  
def pregnancy_generator(c, env):  
    p=pregnancy_probs(c.woman.age/12)
    u=rnd.uniform(0,1)
    if u<=p:
        c.woman.pregnant=True
        env.process(pregnancy_visit(c, env))

        
def live_generator(env):
    while True:
        init_month(env)
        for person in env.persons: 
            monitor(env, person)    
            if not death_generator(person, env):
                env.new_persons.append(person)           
                if person.available:
                    desire=desire_visit(person, env)
                    if desire:
                        env.wanting[person.sex].append(person)
                        for partner in env.wanting[utils.__oposite__(person.sex)]:
                            if partner.available:
                                couple_generator(person, partner, env)
                elif person.partner:
                    if not person.partner.couple_check:
                        c=Couple(person, person.partner)
                        if not c.woman.pregnant:
                            u=rnd.uniform(0,1)
                            ch=how_many_children(u)  
                            if person.childs < ch and person.partner.childs < ch:
                                pregnancy_generator(c, env)
                        rupture_generator(c, env)
                        person.couple_check=True
                    else:
                        person.partner.couple_check=False
                person.age+=1   
            
        env.persons=env.new_persons
        env.new_persons=[]
        env.wanting={'F':[],'M':[]}
        yield env.timeout(1)
    


    
    
        
    
        

        
        
    
    
        

        
        
        