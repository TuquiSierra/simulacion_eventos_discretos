from matplotlib import pyplot as plt
import utils

def plot_stats(env):
    total=utils.__elem_sum__(env.obs_pop['F'], env.obs_pop['M'])
    anhos=len(total)/12
    env.borns=[[sum(env.borns[b:b+12])] for i, b in enumerate(env.borns) if i%12==0]
    env.deaths=[d for i, d in enumerate(env.deaths) if i%12==0]
    f=plt.figure(figsize=(17, 17)) 
    _plot(f,1,2, 3,[(total, 'Población', 'green')], title=f'Evolución de la población \n en {anhos} años', xlabel='Meses')
    _plot(f,2,2, 3,[(env.obs_pop['F'], 'Mujeres', 'pink'), (env.obs_pop['M'], 'Hombres', 'blue')], title=f'Evolución de la población \n por sexos en {anhos} años', xlabel='Meses')
    _plot(f,3,2, 3,[(env.borns, 'Nacimientos', 'orange'),(env.deaths, 'Muertes', 'black')], title=f'Evolución de la relación \n nacimientos-muertes en {anhos} años', xlabel='Años', scatter=True)
    _plot(f,4,2, 3,[(env.average_age, 'Edad promedio', 'green')], title=f'\n Evolución de la \n edad promedio en {anhos} años', xlabel='Meses')
    _plot(f,5,2, 3,[(env.couples, 'Cantidad de parejas', 'pink')], title=f'\n Evolución de la \n cantidad de parejas en {anhos} años', xlabel='Meses')
    plt.show()

def colors():
    return plt.colormaps()

def histogram(x):
    plt.hist(x, bins=25, label=r'Se puede ajustar a una normal \n $\alpha=0.01$')
    plt.show()


def _plot(f,i, r, c, pop, **kwargs):
    sp=f.add_subplot(r,c, i)
    try:
        sp.set_xlabel(kwargs['xlabel'])
    except KeyError:
        pass 
    try:
        sp.set_ylabel(kwargs['ylabel'])
    except KeyError:
        pass

    try:
        sp.title.set_text(kwargs['title'])
    except KeyError:
        pass
        
                
    for p, l, c in pop:       
        try:
            scatter=kwargs['scatter']
            if scatter:
                sp.scatter([i for i in range(len(p))],p,marker='o', label=l, color=c)
            else:
                sp.plot([i for i in range(len(p))],p,'r', label=l, color=c)
        except KeyError:      
            sp.plot([i for i in range(len(p))],p,'r', label=l, color=c)
    sp.legend()
    sp.grid() 

    