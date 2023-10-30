
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
#order pizza
while True:
    order = int(input("\nMasukkan nomor pizza yang anda pesan : ")) #input pemesanan pizza
    if order == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
        bill += 43636
    else:
        print("format yang anda masukkan salah!")
        break
    crust = input("Masukkan nomor pilihan crust : ") #input pilihan crust
    if crust == '1':
        bill += 0
    elif crust == '2':
        bill += 11819
    elif crust == '3':
        bill += 9091
    elif crust == '4':
        bill += 13637
    else:
        print("Format yang anda masukkan tidak sesuai!")
        break
    ukuran = input("Masukkan nomor pilihan ukuran pizza : ") #input pilihan ukuran
    if ukuran == '1':
        bill += 0
        ekstra_cheese = input("apakah anda ingin Ekstra cheese? (y/n) : ")
        if ekstra_cheese == 'y':
            bill += 13636
        else:
            bill += 0
    elif ukuran == '2':
        bill += 57273
        ekstra_cheese = input("apakah anda ingin Ekstra cheese? (y/n) : ")
        if ekstra_cheese == 'y':
            bill += 16364
        else:
            bill += 0
    elif ukuran == '3':
        bill += 89091
        ekstra_cheese = input("apakah anda ingin Ekstra cheese? (y/n) : ")
        if ekstra_cheese == 'y':
            bill += 19091
        else:
            bill += 0
    else:
        print("Format yang anda masukkan tidak sesuai!")
        break
    lanjut = input("pesan yang lain? (y/n) : ")
    if lanjut =='n':
        break
print(f"""\nTerima kasih telah menggunakan layanan Pizza Hut delivery
total tagihan anda adalah : Rp{bill}""")



