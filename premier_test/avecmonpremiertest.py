#! /bin/env python3
# -*- coding: utf-8 -*-

import re, datetime
from django.db import models
from monappli.models import Client,Page,Hit

from django.core.exceptions import ObjectDoesNotExist


mois = {"Jan": 1, "Feb": 2, "Dec": 12}
pattern = re.compile(r'^(\S+).+\[(\d{2})/(\w{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) .*"(?:GET|POST) (.*?) HTTP.*?".*?"(.*?)"')


echecs=[]
with open("/users/2021ds/192001678/Documents/access.log",encoding="utf-8") as f:
    for line in f:
        found = pattern.search(line.strip())
        if not found:
          echecs += [line]
          continue

        # création du client
        ip = found.group(1)
        try :
            cl = Client.objects.get(client_ip=ip)
        except ObjectDoesNotExist as err : 
            cl = Client(client_ip=ip)
            cl.save()
            print(f"ajout: ip={ip}")

        # création de la page
        page = found.group(8)
        try : 
            p=Page.objects.get(page_url=page)
        except ObjectDoesNotExist as err : 
            p=Page(page_url=page)
            p.save()
            print(f"ajout: page={page}")

        # création du hit
        (d,m,y,H,M,S) = found.groups()[1:7]
        ref = found.group(9)
        dt = datetime.datetime(int(y),mois[m],int(d),int(H),int(M),int(S))
        h = Hit(timestamp=dt,referer=ref,client=cl,page=p)
        h.save()

print(f"{len(echecs)} lignes écartées")