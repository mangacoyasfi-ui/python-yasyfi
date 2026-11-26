print("=== jenis pelanggan ===")
print("1.member")
print("2.non member")

pelanggan=int(input("masukan jenis:"))

match pelanggan:
    case 1:
        total=int(input("masukan jumlah belanja:"))  
        if total>=100000:
             print("mendapatkan diskon 10%")
        else:
             print("maaf,anda tidak mendapatkan diskon")
    case 2:
            total=int(input("masukan jumlah belanja:"))  
            if total>=100000:
                 print("selamat,anda mendapatkan diskon 5%")
            else:
                 print("maaf,anda tidak mendapatkan diskon")
    case _:
           print("error")
            