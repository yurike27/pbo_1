while True:
    name_siswa = input("Masukan Nama Anda : ")
    nilai_harian = int(input("Masukan Nilai Harian : "))
    nilai_uts = int(input("Masukan Nilai Uts : "))
    nilai_uas = int(input("Masukan Nilai Uas : "))
    nilai_akhir = int(nilai_harian*40/100)+(nilai_uts*30/100)+(nilai_uas*30/100)

    if nilai_akhir >= 85:
        predikat_nilai ='Amat Baik'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("predikat Anda = ", predikat_nilai)

    elif nilai_akhir >=75:
        predikat_nilai = "Cukup Baik"
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("predikat Anda = ", predikat_nilai)

    elif nilai_akhir >=65:
        predikat_nilai = "Cukup"
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("predikat Anda = ", predikat_nilai)

    elif nilai_akhir >=55:
        predikat_nilai = "Kureng"
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("predikat Anda = ", predikat_nilai)

    else:
        predikat_nilai = "Kureng Sekali"
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("predikat Anda = ", predikat_nilai)

