print("=== PEMILIHAN FILM BIOSKOP ===")

usia = int(input("Masukkan usia pengunjung: "))

if usia >= 17:
    print("\nPilih Genre Film:")
    print("1. Horor")
    print("2. Komedi")
    print("3. Keluarga")
    print("4. Aksi")
    genre = input("Masukkan pilihan genre: ")

    if genre == "1":
        print("\nPilih jenis film:")
        print("1. Horor Indonesia")
        print("2. Horor Luar Negeri")
        jenis = input("Pilihan: ")

        if jenis == "1":
            film = "Horor Indonesia"
        else:
            film = "Horor Luar Negeri"

    elif genre == "2":
        print("\nPilih jenis film:")
        print("1. Komedi Indonesia")
        print("2. Komedi Luar Negeri")
        jenis = input("Pilihan: ")

        if jenis == "1":
            film = "Komedi Indonesia"
        else:
            film = "Komedi Luar Negeri"

    elif genre == "3":
        print("\nPilih jenis film:")
        print("1. Keluarga Indonesia")
        print("2. Keluarga Luar Negeri")
        jenis = input("Pilihan: ")

        if jenis == "1":
            film = "Keluarga Indonesia"
        else:
            film = "Keluarga Luar Negeri"

    elif genre == "4":
        print("\nPilih jenis film:")
        print("1. Hollywood")
        print("2. Indonesia")
        print("3. Bollywood")
        jenis = input("Pilihan: ")

        if jenis == "1":
            film = "Hollywood"
        elif jenis == "2":
            film = "Aksi Indonesia"
        elif jenis == "3":
            film = "Bollywood"
        else:
            film = "Crime"

    else:
        film = "Romance"

else:
    print("\nPilih Jenis Animasi:")
    print("1. Animasi 2 Dimensi")
    print("2. Animasi 3 Dimensi")

    animasi = input("Masukkan pilihan: ")

    if animasi == "1":
        print("\nPilih Film:")
        print("1. Naruto")
        print("2. One Piece")
        pilihan = input("Masukkan pilihan film: ")

        if pilihan == "1":
            film = "Naruto"
        elif pilihan == "2":
            film = "One Piece"
        else:
            film = "Aot"

    elif animasi == "2":
        print("\nPilih Film:")
        print("1. Nemo")
        print("2. Kungfu Panda")
        pilihan = input("Masukkan pilihan film: ")

        if pilihan == "1":
            film = "Nemo"
        elif pilihan == "2":
            film = "Kungfu Panda"
        else:
            film = "Cars3"

    else:
        film = "Upin ipin"

if film != "":
    print("\nSelamat Menyaksikan", film)
else:
    print("\nPilihan tidak tersedia!")