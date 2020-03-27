import simpy
import random as rnd
from person import Woman, Man
from my_globals import G
from process import live_generator
import math
import plotting 
import utils 
from sys import argv  
    
def evolve(M, H, plot=False):
    env=simpy.Environment()
    env.persons=[]
    env.obs_pop={'F':[], 'M':[]}
    env.new_persons=[]
    env.wanting={'F':[],'M':[]}
    env.borns=[]
    env.deaths=[]
    env.average_age=[]
    env.couples=[]
    
    for i in range(M):
        w=Woman(i)
        env.persons.append(w)
        w.age=rnd.randint(0,1200)
    
    j=len(env.persons)
    
    for i in range(H):
        m=Man(i+j)
        env.persons.append(m)
        m.age=rnd.randint(0,1200)
    
    env.idx=M+H
         
    env.process(live_generator(env))
    env.run(G.max_time)
    tot_pop=utils.__elem_sum__(env.obs_pop['F'], env.obs_pop['M'])
    
    if plot:  
        env.average_age=[elem/(tot_pop[i]*12) for i, elem in enumerate(env.average_age)]
        plotting.plot_stats(env)
        
    return tot_pop

M=int(argv[1])
H=int(argv[2])
try:
    anhos=int(argv[3])
except:
    G.max_time=anhos

evolve(M, H, plot=True)



        
        
           