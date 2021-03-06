#!/bin/env python3
import getlist, sys
"""
    Soit L le type liste dont les éléments sont soit tous de type int, soit tous de type L.
    Par exemple, l = [ [1,2], [ [2,3,4], [5,4,3,2], [[3,1],[2]]], [0,9] ] est de type L.  
    Ce programme est appelé avec une liste de type L sur la ligne de commande,
    et sort le min des max de ses sous-listes.  
    Avec la liste l ci-dessus, la liste des max est [2, 4, 5, 3, 2, 9] donc le programme sort 2.
    La liste doit être fournie sous la forme : [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
"""

def minmax(l):
    """
    Cette fonction récursive retourne le minmax de la liste passée en argument.
    """
    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)
if __name__=="__main__":
    # programme principal
    if len(sys.argv)==1:
        pass
    elif len(sys.argv)==2:
        pass
    else :
        getlist.i=1
        l = getlist.construire()                   # récupération de la liste
    maxi = []
    minmax(l)
    print(min(maxi))
