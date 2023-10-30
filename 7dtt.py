
print("\nProgram Order Pizza Otomatis")
#print menu
print("""\n
      ----------------------------
      |NO|      NAMA PIZZA       |
      ----------------------------
      |1 |    Frankfurter BBQ    |
      |2 |      Meat Monsta      |
      |3 |  American Favourite   |
      |4 |     Meat Lovers       |
      |5 |    Chicken Lovers     |
      |6 |     Super Supreme     |
      |7 | Super Supreme Chicken |
      |8 |     Cheese Lovers     |
      ----------------------------
      \n
      ----------------------------
      |NO|     PILIHAN CRUST     |
      ----------------------------
      |1 |         Pan           |
      |2 | StuffedCrusted Cheese |
      |3 |StuffedCrusted Saussage|
      |4 |    Cheesey Bite       |
      ----------------------------
      \n
       ----------------------------
      |NO|       UKURAN          |
      ----------------------------
      |1 |       Personal        |
      |2 |       Reguler         |
      |3 |        Large          |
      ----------------------------""")

bill = 0

order = input("\nMasukkan nomor pizza yang anda pesan : ")
if order in ['1', '2', '3', '4', '5', '6', '7', '8']:
    bill += 43636
else:
    print ("Format yang anda masukkan tidak sesuai!")
    
crust = input ("Masukkan nomor pilihan crust : ")
if crust == '1' :
    bill += 0
elif crust == '2' :
    bill += 11819
elif crust == '3' :
    bill += 9091
elif crust == '4' :
    bill += 13637
else: 
    print("Format yang anda masukkan tidak sesuai!")
    


