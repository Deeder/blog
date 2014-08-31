import numpy as np

def repartirVoiture(n):
    '''Repartition aleatoire des voitures pour n emissions'''
    voitures = np.random.randint(0, 3, n)
    return voitures

def simulerChoixCandidat(n, mode='random'):
    '''Simulation des choix des candidats pour n emissions (soit aleatoire, soit toujours le meme)'''
    if mode is not 'random':
        choix = np.array([1]*n)
    else:
        choix = np.random.randint(0, 3, n)
    return choix

def ouvrirPorte(prix, choix):
    '''Ouverture d'une porte par le presentateur en fonction de la position de la voiture et du choix du candidat'''
    portesOuvertes = np.zeros(choix.shape)
    for i, x in enumerate(prix):
        for k in [0, 1, 2]:
            if k != x and k != choix[i]:
                portesOuvertes[i] = k
    return portesOuvertes

def changerChoix(choix, portesOuvertes):
    '''Le candidat decide de changer de choix apres l'ouverture de la porte par le presentateur'''
    secondChoix = np.zeros(choix.shape)
    for i, x in enumerate(portesOuvertes):
        for k in [0, 1, 2]:
            if k != x and k != choix[i]:
                secondChoix[i] = k
    return secondChoix

def afficherResultats(choixFinal, prix):
    '''Afficher les taux de gain en pourcentages'''
    mask = choixFinal == prix
    pc = mask.sum() / float(len(mask)) * 100
    return pc

n = 10000
choix          = simulerChoixCandidat(n)
prix           = repartirVoiture(n)
portesOuvertes = ouvrirPorte(prix, choix)
secondChoix    = changerChoix(choix, portesOuvertes)
print 'Reussite sans changement : %0.2f%%' % afficherResultats(choix, prix)
print 'Reussite avec changement : %0.2f%%' % afficherResultats(secondChoix, prix)