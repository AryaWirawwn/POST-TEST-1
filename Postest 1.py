import math
def login():
    while True:
        print('-----Selamat datang silahkan login-----')
        nama = input('Masukkan Nama: ')
        nim = input('Masukkan NIM: ')
        pin = input('Masukkan Pin: ')
        if nama == 'Arya' and nim == '027' and pin == '0709':
            print('Selamat datang')
            return True
        elif nama == 'Arya' or nim == '027' or pin == '0709':
            print('Ada data yang dimasukkan salah, coba lagi')
        else:
            print('Data yang dimasukkan salah, coba lagi')

def menu():
    login_berhasil = login()
    if login_berhasil:
        print('Selamat datang di Program Segitiga Pythagoras')
        selesai = False
        while not selesai:
            print('1. Hitung alas')
            print('2. Hitung sisi tegak')
            print('3. Hitung sisi miring')
            print('4. Keluar')
            menu_hitung = int(input('Apa yang ingin anda hitung: '))
            if menu_hitung == 1:
                sisi_miring = int(input('Masukkan sisi miring: '))
                sisi_tegak = int(input('Masukkan sisi tegak: '))
                if sisi_miring >= sisi_tegak:
                    rumus_alas = math.sqrt(sisi_miring**2 - sisi_tegak**2)
                    print(f'Hasil alas adalah {rumus_alas}')
                else:
                    print('Sisi miring harus lebih dari sama dengan sisi tegak')
                lanjut=input('lagi? (ya/tidak) : ')
                if lanjut == 'tidak':
                    print('Terima Kasih sudah menggunakan kalkulator ini')
                    selesai = True
            
            elif menu_hitung == 2:
                sisi_miring = int(input('Masukkan sisi miring: '))
                alas = int(input('Masukkan alas: '))
                if sisi_miring >= alas:
                    rumus_sisi_tegak = math.sqrt(sisi_miring**2 - alas**2)
                    print(f'Hasil sisi tegak adalah {rumus_sisi_tegak}')
                else:
                    print('Sisi miring harus lebih dari sama dengan alas')
                lanjut=input('lagi? (ya/tidak) : ')
                if lanjut == 'tidak':
                    print('Terima Kasih sudah menggunakan kalkulator ini')
                    selesai = True
            
            elif menu_hitung == 3:
                alas = int(input('Masukkan alas: '))
                sisi_tegak = int(input('Masukkan sisi miring: '))
                rumus_sisi_miring = math.sqrt(alas**2 + sisi_tegak**2)
                print(f'Hasil sisi tegak adalah {rumus_sisi_miring}')
                lanjut=input('lagi? (ya/tidak) : ')
                if lanjut == 'tidak':
                    print('Terima Kasih sudah menggunakan kalkulator ini')
                    selesai = True
            
            elif menu_hitung == 4:
                print('Terima Kasih sudah menggunakan kalkulator ini')
                selesai = True
            
            else:
                print('Tidak ada menu untuk angka >=5')

menu()