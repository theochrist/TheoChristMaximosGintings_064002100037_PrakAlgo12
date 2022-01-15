def BubbleSort(obj):
    n = len(obj)
    for z in range(n):
        for x in range(0, n-z-1):
            if obj[x] > obj[x + 1]:
                obj[x], obj[x + 1] = obj[x + 1], obj[x]

jumlahAngka = int(input("Masukkan jumlah angka pada list: "))
listAngka = [int(input(f"Masukkan angka ke-{x+1}: ")) for x in range(jumlahAngka)]

print(f"\nList angka -> {listAngka}")
BubbleSort(listAngka)
print(f"Hasil Bubble Sort -> {listAngka}")