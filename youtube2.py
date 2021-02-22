#71200593_Dedi Yanto
#Universitas Kristen Duta Wacana
#Prodi Teknik Informatika
#Struktur Kontrol Percabangan

'''Soal
Pada suatu hari Adik Todoroki yang sedang duduk di bangku kelas 3 SD yang bernama Mai 
kesulitan memahami pelajaran perbandingan dan aritmatika dasar, karena Todoroki adalah seorang programmer, 
Mai meminta bisakah Todoroki untuk membuat sebuah program sederahana yang dapat membantu 
Mai dalam belajar perbandingan sekaligus aritmatika dasar. Mai meminta program bisa 
membandingkan apakah angka negatif dan positif itu adalah (>/</=), kemudian menggabungkan 
aritmatika dasar yang berupa(+,-,x,/) kepada angka dan membandingkan nya seperti contoh 
apakah 4 + 2 < 10-4?. Cobalah untuk membuat program yang sesuai dengan keperluan Mai
Keperluan mei adalah
1. belajar aritmatika dasar
2. belajar perbandingan yang digabungkan dengan aritmatika dasar
3. angka dan operasi yang keluar acak karena mai ingin melatih kemampuannya
'''
'''
input:
1. Aritmatika dasar
2. Perbandingan
input: aritmatika dasar
input jawaban: dua puluh tujuh
proses:


output:1
1. soal yang acak, dan angkat yang acak tentang arimatika dasar
24 + 5 = berapa

salah
29

silahkan memilih antara 1/2 
silahkan masukan jawaban dengan angka.

test case:
Test case
1.	Memasukkan angka diluar pilihan 1 dan 2, dan kalimat
2.	Memasukkan pilihan 1. Aritmatika dasar. Kemudian menjawab dengan salah dan benar,
 dan kemudia memasukkan angka dengan ,(koma) dan kalimat
3.	Memasukkan pilihan 2. Perbandingan, mencoba masing masing perbandingan,
Dengan salah, dan dengan benar dan dengan kalimat.

'''
#Proses pembuatan source Code
print("Selamat datang di Program Quiz Operasi Aritmatika dan perbandingan\n")
import random
op = ['>','<','=']
angka1 = random.randint(-15,15)
angka2 = random.randint(-15,15)
angka3 = random.randint(-15,15)
lvl1 = [str(angka1)+'+'+str(angka3),str(angka1)+'-'+str(angka3),str(angka1)+'*'+str(angka3),str(angka1)+'/'+str(angka3)]
lvl2 = [str(angka2)+'+'+str(angka3),str(angka2)+'-'+str(angka3),str(angka2)+'*'+str(angka3),str(angka2)+'/'+str(angka3)]
acak1 = random.choice(op)
acak2 = random.choice(lvl1)
acak3 = random.choice(lvl2)

pilihan = input("Operasi apa yang ingin anda coba\n1.Aritmatika Dasar\n2.Perbandingan\n:")

try:
    jawaban = int(pilihan)
    if jawaban == 1:
        print("Berapakah hasil dari,",acak2,"+",acak3," ?\n")
        print("(Jika jawaban adalah angkaa desimal bulatkan menjadi 2 angka dibelakang koma)")
        hasil = round(eval(acak2)+eval(acak3),2)
        jwban = input("Masukkan jawaban anda: ")
        try:
            jwb = float(jwban)
            if jwb == hasil:
                print("Selamat Jawaban Anda Benar!!")
            else:
                print("Jawaban Anda Salah!!")
                print("Jawaban yang benar adalah ",hasil)
        except:
            print("Silahkan masukkan jawaban dengan angka dan koma dengan tiitk(.)!!")
    elif jawaban == 2:
        if acak1 == '>':
            hasil = eval(acak2) > eval(acak3)
            print("\nApakah hasil dari ",acak2,"Lebih besar dari hasil",acak3," ?\n")
            jwban = input("Masukkan jawaban anda:\n1.Benar\n2.Salah\n:")
            try:
                jwb = int(jwban)
                if jwb == 1:
                    if hasil == True:
                        print("Selamat Jawaban Anda Benar!!")
                    elif hasil == False:
                        print("Jawaban yang Anda berikan Salah!!")
                        print("Nilai",acak2,"Lebih kecil dari nilai",acak3)
                elif jwb == 2:
                    if hasil == True:
                        print("Jawaban yang Anda berikan Salah!!")
                        print("Nilai",acak2,"Lebih besar dari nilai",acak3)
                    elif hasil == False:
                        print("Selamat Jawaban Anda Benar!!")
                else:
                    print("Pilihan jawaban hanya tersedia 1. benar dan 2. salah")
            except:
                print("Silahkan masukkan jawaban dengan angka 1 atau 2")
        elif acak1 == '<':
            hasil = eval(acak2) < eval(acak3)
            print("\nApakah hasil dari ",acak2,"Lebih kecil dari hasil",acak3," ?\n")
            jwban = input("Masukkan jawaban anda:\n1.Benar\n2.Salah\n:")
            try:
                jwb = int(jwban)
                if jwb == 1:
                    if hasil == True:
                        print("Selamat Jawaban Anda Benar!!")
                    elif hasil == False:
                        print("Jawaban yang Anda berikan Salah!!")
                        print("Nilai",acak2,"Lebih besar dari nilai",acak3)
                elif jwb == 2:
                    if hasil == True:
                        print("Jawaban yang Anda berikan Salah!!")
                        print("Nilai",acak2,"Lebih kecil dari nilai",acak3)
                    elif hasil == False:
                        print("Selamat Jawaban Anda Benar!!")
                else:
                    print("Pilihan jawaban hanya tersedia 1. benar dan 2. salah")
            except:
                print("Silahkan masukkan jawaban dengan angka 1 atau 2")
        elif acak1 == '=':
            hasil = eval(acak2) == eval(acak3)
            print("\nApakah hasil dari ",acak2,"sama dengan hasil",acak3," ?\n")
            jwban = input("Masukkan jawaban anda:\n1.Benar\n2.Salah\n:")
            try:
                jwb = int(jwban)
                if jwb == 1:
                    if hasil == True:
                        print("Selamat Jawaban Anda Benar!!")
                    elif hasil == False:
                        print("Jawaban yang Anda berikan Salah!!")
                        print("Nilai",acak2,"Tidak sama dengan hasil ",acak3)
                elif jwb == 2:
                    if hasil == True:
                        print("Jawaban yang Anda berikan Salah!!")
                        print("Nilai",acak2,"Sama dengan hasil",acak3)
                    elif hasil == False:
                        print("Selamat Jawaban Anda Benar!!")
                else:
                    print("Pilihan jawaban hanya tersedia 1. benar dan 2. salah")
            except:
                print("Silahkan masukkan jawaban dengan angka 1 atau 2")
    else:
        print("Pilihan Operasi hanya tersedia 1. Arimatika dan 2. Perbandingan")
except:
    print("Silahkan masukkan jawaban dengan angka 1 atau 2 !!!")