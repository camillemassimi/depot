import sys

i=1

def construire():
    """
    Cette fonction récursive construit la liste 
    à partir des arguments fournis sur la ligne de commande.
    Elle retourne la liste construite.
    """

    global i  
    l = []          
    while True:
        if sys.argv[i]=="[":   
            i+=1               
            if i!=2:                  # pour la première liste, on ne fait rien
                l.append(construire()) 
        elif sys.argv[i]=="]":        # c'est la fin de la liste,
            i+=1
            return l                  # on renvoie la liste constuite
        else:                         # c'est une liste d'entiers
            l.append(int(sys.argv[i]))   
            i+=1

def mklist():
    global i
    l = []          # liste courante
    while True:
        if lline[i]=="[":   # c'est une liste de listes
            i+=1                 # argument suivant
            if i!=1:             # pour la première liste, on ne fait rien
                l.append(mklist())    # sinon on construit cette sous-liste et on la met dans la liste courante
        elif lline[i]=="]": # c'est la fin de la liste,
            i+=1
            return l             # on renvoie la liste courante
        else:                  # c'est une liste d'entiers
            l.append(int(lline[i]))   
            i+=1

def build(l0):
    """
    Cette fonction construit la liste correspondant à sa représentation chaine de caractère fourni en argument.
    """

    def _build():
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1                 
                if i!=1:             # pour la première sous-liste, on ne fait rien
                    l.append(_build())    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))   
                i+=1
    i = 0
    res = _build()
    return res