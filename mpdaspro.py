print('Selamat datang di mpdaspro')
print('Silahkan login terlebih dahulu')

username = input('buat username: ')
password = input('buat password: ')
print('\n------ DATA DIKONFIRMASI ------')

username2 = input('username: ')
password2 = input('password: ')

if username == username2 and password == password2:
    print('\nanda berhasil login')
    ulang = "y"
    while ulang.lower() == "y":
        jam_kerja = int(input('masukkan jam kerja: '))
        tarif = int(input('masukkan tarif: '))  
        if jam_kerja > 160:
            total = jam_kerja * tarif
            bonus = total * 0.1  # Menghitung bonus 10%
            print(f'total: {total + bonus}')  # Menggunakan f-string untuk menghindari tuple
        else:
            total = jam_kerja * tarif
            print(f'total: {total}')  # Gunakan f-string di sini juga

        ulang = input('Apakah anda ingin mengulang? (y/n) ')
    print('Terima kasih')
else:
    print('Anda gagal login')



