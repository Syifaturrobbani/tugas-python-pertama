# ==================================================================================
'''Fungsi untuk mengecek apakah angka ganjil atau genap.
tugas soal pertama

program input number secara manual'''
# ==================================================================================


import math
def cek_ganjil_genap(*angka):
    angka = angka[0]
    if angka % 2 == 0:
        return ("genap")
    else:
        return ("ganjil")


# ==================================================================================
''' exit '''
# ==================================================================================


# ==================================================================================
'''Fungsi untuk mengecek apakah tahun kabisat atau bukan. '''
# ==================================================================================

def cek_tahun_kabisat(*tahun):
    tahun = tahun[0]
    if tahun % 400 == 0:
        return True
    if tahun % 100 == 0:
        return False
    if tahun % 4 == 0:
        return True
    return False


# ==================================================================================
''' exit '''
# ==================================================================================


# ==================================================================================
'''
Fungsi untuk menghitung luas lingkaran.
Guna fungsi math.pi untuk menghitung nilai pi.
program ini si user bisa input number bebas'''
# ==================================================================================


def hitung_luas_lingkaran(*jari_jari):
    jari_jari = jari_jari[0]
    jari_jari = int(jari_jari)
    luas_lingkaran = math.pi*(jari_jari*jari_jari)
    return float(luas_lingkaran)


# ==================================================================================
''' exit '''
# ==================================================================================


# ==================================================================================
''' Fungsi untuk menghitung volume kubus. '''
# ==================================================================================


def hitung_volume_kubus(*panjang_rusuk):
    panjang_rusuk = panjang_rusuk[0]
    panjang_rusuk = int(panjang_rusuk)
    hasil = panjang_rusuk ** 3
    return hasil


# ==================================================================================
''' exit '''
# ==================================================================================


# ==================================================================================
''' Fungsi untuk menghitung rerata dari list angka. '''
# ==================================================================================


def hitung_rerata(*list_angka):
    list_angka = list_angka[0]
    n = len(list_angka)
    s = sorted(list_angka)
    return float((s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None)


# ==================================================================================
''' exit '''
# ==================================================================================


# ==================================================================================
'''  menghitung jumlah huruf vokal dalam sebuah kalimat. '''
# ==================================================================================


def hitung_huruf_vokal(*kalimat):
    kalimat = kalimat[0 ]
    kalimat = str(kalimat)
    kata = "AIUEOaiueo"
    jumlahkarakter = ""
    for i in kalimat:
        if i not in kata:
            jumlahkarakter += i
    print(len(jumlahkarakter))


# ==================================================================================
''' exit '''
# ==================================================================================

# ==================================================================================
'''  mencari angka terbesar dari list angka. '''
# ==================================================================================


def cari_angka_terbesar(list_angka):
    angka = list_angka[0]

    if len(list_angka) > 1:

        next_angka = cari_angka_terbesar(list_angka[1:])

        if next_angka > angka:
            angka = next_angka

    return angka


# ==================================================================================
''' exit '''
# ==================================================================================


# ==================================================================================
'''  mencari angka yang duplikat dalam list angka. '''
# ==================================================================================


def cari_angka_duplikat(*list_angka):
    list_angka = list_angka[0]
    seen = set()
    seen_add = seen.add
    seen_twice = set(x for x in list_angka if x in seen or seen_add(x))
    return list(seen_twice)


# ==================================================================================
''' exit '''
# ==================================================================================


# ==================================================================================
'''  menghitung faktorial dari sebuah angka. '''
# ==================================================================================


def hitung_faktorial(*angka):
    angka = angka[0]
    angka = int(angka)
    if angka > 2:
        return angka * hitung_faktorial(angka - 1)
    return angka


# ==================================================================================
''' exit '''
# ==================================================================================

# ==================================================================================
'''  untuk menghitung jumlah setiap karakter dalam sebuah kata.. '''
# ==================================================================================


def hitung_jumlah_setiap_karakter(*kata):
    kata = kata[0]
    freq = {}
    for c in set(kata):
        freq[c] = kata.count(c)
    return {c: kata.count(c) for c in set(kata)}


# ==================================================================================
''' exit '''
# ==================================================================================