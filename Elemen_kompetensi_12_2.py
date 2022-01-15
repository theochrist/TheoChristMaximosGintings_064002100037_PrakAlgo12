print("Linear Search")

jumlahAngka = int(input("Masukkan jumlah angka pada list: "))
listAngka = [int(input(f"Masukkan angka ke-{x+1}: ")) for x in range(jumlahAngka)]

print(f"\nList Angka -> {listAngka}")
cariAngka = int(input("Masukkan angka yang dicari: "))
for x in listAngka:
    if x == cariAngka:
        print(f"Hasil Linear Search -> Ditemukan pada index ke-{listAngka.index(x)}")
        exit(0)

print("Hasil Linear Search -> Tidak Ditemukan")