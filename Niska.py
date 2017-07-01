# -*- coding: utf-8 -*-

niska = "Milena je sinoć videla Mitra, nežnog, zelenog skakavca ispred stacionara i uzviknula je: \"Ju, Mitre, uplašio si me!\"."
niska = niska.lower()
reci = niska.split(" ")
print(reci)

reci[4] = reci[4][:-1]
print(reci[4])
 
reci[5] = reci[5][:-1]
print(reci[5])

reci[12] = reci[12][:-1]
print(reci[12])

reci[13]=reci[13][1:-1]
print(reci[13])

reci[14]=reci[14][:-1]
print(reci[14])

reci[17]=reci[17][:-3]
print(reci[17])

lista = reci[:]
print(lista)

