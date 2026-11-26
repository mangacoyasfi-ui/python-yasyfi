print("=== masukan no menu ===")
print("1.es teh.Rp5.000")
print("2.es jeruk.Rp7.000")
print("3.kopi.Rp8.000")
print("4.susu.RP6.000")

angka=int(input("masukan angka:"))

match angka:
    case 1:
        print("1.es teh.Rp5.000")
    case 2:
            print("2.es jeruk.RP7.000")
    case 3:
            print("3.kopi.Rp8.000")
    case 4:
            print("4.susu.Rp.6.000")
    case _:
            print("menu tidak tersedia")