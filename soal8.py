print("=== pilih kategori ujian ===")
print("1.teori")
print("2.praktek")

kategori=int(input("masukan kategori:"))

match kategori:
    case 1:
        nilai=int(input("masukan nilai:"))  
        if nilai>=75:
             print("selamat,anda lulus")
        else:
             print("maaf,anda belum lulus")
    case 2:
            nilai=int(input("masukan nilai:"))  
            if nilai>=75:
                 print("selamat,anda lulus")
            else:
                 print("maaf,anda belum lulus")
    case _:
           print("bulan tidak tersedia")