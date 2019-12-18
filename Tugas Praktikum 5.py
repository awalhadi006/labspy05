nim = []
nama = []
tugas = []
uts = []
uas = []
nakhir = []

print("Program Input Nilai")
print("===================")
pilihan = 1
while pilihan != 0:
    pilihan = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar] :")
    if pilihan == "T":
        print("\nTambah Data")
        masnim = input("NIM\t\t\t : ")
        nim.append({'nim': masnim})
        masnama = input("NAMA\t\t : ")
        nama.append({'nama': masnama})
        masuts = int(input("Nilai UTS\t : "))
        uts.append({'uts': masuts})
        masuas = int(input("Nilai UAS\t : "))
        uas.append({'uas': masuas})
        mastugas = int(input("Nilai Tugas\t : "))
        tugas.append({'tugas': mastugas})
        akhir = (30 * mastugas / 100) + (35 * masuts / 100) + (35 * masuas / 100)
        nakhir.append({'nakhir': akhir})

    elif pilihan == "L":
        no = 0
        if len(nim) != 0:
            print("\nDaftar Nilai")
            print("======================================================================================")
            print("| No |     NIM     |    NAMA    |    TUGAS    |    UTS    |    UAS    |    AKHIR     |")
            print("======================================================================================")
            for i in range(len(nim)):
                no = no+1
                print("|" ,no ," | {0:12s}| {1:11.11s}|{2:^13d}|{3:^11d}|{4:^11d}|{5:^14.2f}|".format(nim[i]['nim'],
                    nama[i]['nama'],tugas[i]['tugas'],uts[i]['uts'],uas[i]['uas'],nakhir[i]['nakhir']))
            print("======================================================================================")
        else:
            print("\nDaftar Nilai")
            print("======================================================================================")
            print("| No |     NIM     |    NAMA    |    TUGAS    |    UTS    |    UAS    |     AKHIR    |")
            print("======================================================================================")
            print("|                                TIDAK ADA DATA                                      |")
            print("======================================================================================")

    elif pilihan == "U":
        masnim = input("Masukkan NIM yang ingin diubah datanya : ")
        for i in range(len(nim)):
            if masnim == nim[i]['nim']:
                masnimnew = input("NIM\t\t\t : ")
                nim[i]['nim'] = masnimnew
                masnamanew = input("Nama\t\t : ")
                nama[i]['nama'] = masnamanew
                masutsnew = int(input("Nilai UTS\t : "))
                uts[i]['uts'] = masutsnew
                masuasnew = int(input("Nilai UAS\t : "))
                uas[i]['uas'] = masuasnew
                mastugasnew = int(input("Nilai Tugas\t : "))
                tugas[i]['tugas'] = mastugasnew
                akhirnew = (30 * mastugasnew / 100)+(35 * masutsnew / 100)+(35 * masuasnew / 100)
                nakhir[i]['nakhir'] = akhirnew
                break
            print("NIM", masnim, "Tidak Ditemukan")

    elif pilihan == "H":
        masnim = input("masukan nim : ")
        for i in range(len(nim)):
            if masnim == nim[i]['nim']:
                print("Data dengan NIM : ", nim[i]['nim'], "Telah Dihapus.")
                del nim[i]
                del nama[i]
                del tugas[i]
                del uts[i]
                del uas[i]
                del nakhir[i]
                break
            print("NIM", masnim, "Tidak Ditemukan")

    elif pilihan == "C":
        masnim = input("Masukkan NIM yang ingin di cari datanya : ")
        for i in range(len(nim)):
            if masnim == nim[i]['nim']:
                print("\nDaftar Nilai")
                print("======================================================================================")
                print("| No |     NIM     |    NAMA    |    TUGAS    |    UTS    |    UAS    |    AKHIR     |")
                print("======================================================================================")
                print("|",i++1, " | {0:12s}| {1:11s}|{2:^13d}|{3:^11d}|{4:^11d}|{5:^14.2f}|".format(nim[i]['nim'],nama[i]['nama'],
                        tugas[i]['tugas'],uts[i]['uts'],uas[i]['uas'],nakhir[i]['nakhir']))
                print("======================================================================================")
                break
            print("Nim",masnim,"Tidak Ditemukan")

    elif pilihan == "K":
        exit()

    else:
        print("gunakan hanya kata kunci diatas!! (Huruf Kapital)")
