#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2

conn = psycopg2.connect(host='cmassimi@savennieres.math.univ-angers.fr',database='cmassimi',user='cmassimi',password='116910')
cur=conn.curser()

with open("caracteristiques-2018.csv","r",newline='',encoding="latin-1") as f:
    next(f)
    for ligne in f :
        data = ligne.strip().split(",") #elimine les \n de fin de ligne
        print(data)
        cur.execute("""INSERT INTO accidents.caracteristiques(
        num_acc,an,mois,jour,hrmn,lum,agg,inter,atm,col,com,adr,gps,latitude
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        data)
    conn.commit()


cur.close()
conn.close()