print("=== masukan angka ===")
print("1.januari")
print("2.februari")
print("3.maret")
print("4.april")
print("5.mei")
print("6.juni")

angka=int(input("masukan angka:"))

match angka:
    case 1:
        print("1.januari")
    case 2:
            print("2.februari")
    case 3:
            print("3.maret")
    case 4:
            print("4.april")
    case 5:
            print("5.mei")
    case 6:
            print("6.maret")
    case _:
            print("bulan tidak tersedia")