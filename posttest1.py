import os
os.system("cls")

def flatten (listnya):
    output = []
    for element in listnya:
        if isinstance(element, list) :
            output.extend(flatten(element))
        else:
            output.append(element)
    return output

def mergeSort(list): 
    panjang = len(list) 
    if panjang == 1: 
        return list 
 
    tengah = panjang // 2 
    kiri = mergeSort(list[:tengah]) 
    kanan = mergeSort(list[tengah:]) 
    return merge(kiri, kanan) 

def merge(kiri, kanan): 
    output = [] 
    q = r = 0 
    while q < len(kiri) and r < len(kanan): 
        if kiri[q] < kanan[r]: 
            output.append(kiri[q]) 
            q += 1 
        else: 
            output.append(kanan[r]) 
            r += 1 
    output.extend(kiri[q:]) 
    output.extend(kanan[r:]) 
 
    return output

variabel = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90] 
print('\nSebelum diurutkan =', variabel)
urutan = flatten(variabel)
print('\nSesudah diratakan =', urutan)
hasil = mergeSort(urutan)
print('\nHasil akhir =', hasil)