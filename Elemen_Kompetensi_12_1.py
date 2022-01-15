def SelectionSort(obj):
    n = len(obj)
    for z in range(n):
        minimum = z
        for x in range(z+1, n):
            if obj[minimum] > obj[x]:
                minimum = x
        obj[z], obj[minimum] = obj[minimum], obj[z]

jumlahAngka = int(input("Masukkan jumlah angka pada list: "))
listAngka = [int(input(f"Masukkan angka ke-{x+1}: ")) for x in range(jumlahAngka)]

print(f"\nList angka -> {listAngka}")
SelectionSort(listAngka)
print(f"Hasil Selection Sort -> {listAngka}")