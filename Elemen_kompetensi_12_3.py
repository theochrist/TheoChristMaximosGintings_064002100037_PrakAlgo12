def BinarySearch(obj, halfleft, halfright, search):
    if halfright >= halfleft:
        middle = halfleft + ( halfright - halfleft) // 2
        if obj[middle] == search:
            return middle
        elif obj[middle] > search:
            return BinarySearch(obj, halfleft, middle-1, search)
        else:
            return BinarySearch(obj, middle+1, halfright, search)
    else:
        return -1

jumlahAngka = int(input("Masukkan jumlah angka pada list: "))
listAngka = [int(input(f"Masukkan angka ke-{x+1}: ")) for x in range(jumlahAngka)]

print(f"\nList angka -> {listAngka}")
cariAngka = int(input("Masukkan angka yang dicari: "))
hasil = BinarySearch(listAngka, 0, len(listAngka) - 1, cariAngka)
if hasil != -1:
    print(f"Hasil Binary Search -> Ditemukan pada index ke-{hasil}")
else:
    print("Hasil Binary Search -> Tidak Ditemukan")