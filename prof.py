#!/bin/env python3

#fait appel a un fichier "listes.txt", on doit rentrer la liste dedans

import getlist, re, sys

"""
    Soit L le type liste dont les éléments sont soit tous de type int, soit tous de type L.
    Ce programme est appelé avec le nom d'un fichier sur la ligne de commande,
    ce fichier contenant des listes de type L.
    Il sort la profondeur de chaque liste.
"""

def profondeur(l):
    """
    Cette fonction renvoie la profondeur de la liste passée en argument.
    """

    def _profondeur(l,p):
        nonlocal prof
        for i in l:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)

    prof=float("-inf")
    _profondeur(l,1)
    return(prof)

if __name__=="__main__":
    # programme principal
    if len(sys.argv)==1:
      pass
    elif len(sys.argv)==2:
      f = open("listes.txt", "r")
      for line in f:
          lline = re.split(r' +',line.rstrip("\n"))
          l = getlist.build(lline)                     
          print(f"{l=}")
          print(f"{profondeur(l)=}")
    else:
      pass
