# -*- coding: utf-8 -*-
#2,3,5,7,11,13

sayi= int(input("Sayı giriniz : "))
asalMi = True
if sayi == 0: 
       asalMi = False
if sayi == 1 :
       asalMi = False
if sayi == 2 :
       asalMi = True
else:
  for x in range(2,sayi):
      if(sayi % x) == 0: 
         asalMi = False
         break

if asalMi == True : 
   print("asal")
else:
   print("asal değil")