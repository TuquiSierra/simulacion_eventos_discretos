import plotting
from main_simulation import evolve
from scipy import stats as ss


def simulate(n, M, H):
    simulations=[]
    for _ in range(n):
        simulations.append(evolve(M, H)[-1])
    plotting.histogram(simulations)
    
    media, desviacion = ss.norm.fit(simulations)
    d, pvalor = ss.kstest(simulations,'norm',args=(media, desviacion))

    if pvalor < 0.01:
        print("No se ajusta a una normal con confianza de 99 %")
    else:
        print("Se puede ajustar a una normal con confianza de 99 %")
   
def rupture_changes(H, M, probs):
    results=[]
    c=['red', 'green', 'blue', 'orange']
    for p in probs:
        G.rupture_prob=p
        results.append(evolve(100, 100))
    plotting._plot([(results[i], str(probs[i]), c[i]) for i in range(len(probs))], title=f'Evolución de la población en 100 años \n según probabilidades de ruptura de parejas', xlabel='Meses')
       
       
simulate(1000, 10, 10)