import time


ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']

i0 = 'a'
i1 = 'a'
i2 = 'a'
i3 = 'a'
i4 = 'a'
i5 = 'a'
i6 = 'a'
i7 = 'a'

k = ''
z = 0
temps = time.time()


while k != 'enfants':
    #print(ma_liste[i],ma_liste[j])
    k = ma_liste[i6] + ma_liste[i5] + ma_liste[i4] + ma_liste[i3] + ma_liste[i2] + ma_liste[i1] + ma_liste[i0]
    if z == 100000:
        print(k)
        z = 0
    z += 1
    i0 += 1 # On incrémente i1
    if i0 == 10:
        i0 = 'a'
        i1 += 1
    if i1 == 10:
        i0 = 'a'
        i1 = 'a'
        i2 += 1
    if i2 == 10:
        i0 = 'a'
        i1 = 'a'
        i2 = 'a'
        i3 += 1
    if i3 == 10:
        i0 = 'a'
        i1 = 'a'
        i2 = 'a'
        i3 = 'a'
        i4 += 1
    if i4 == 10:
        i0 = 'a'
        i1 = 'a'
        i2 = 'a'
        i3 = 'a'
        i4 = 'a'
        i5 += 1
    if i4 == 10:
        i0 = 'a'
        i1 = 'a'
        i2 = 'a'
        i3 = 'a'
        i4 = 'a'
        i5 += 1
    if i5 == 10:
        i0 = 'a'
        i1 = 'a'
        i2 = 'a'
        i3 = 'a'
        i4 = 'a'
        i5 = 'a'
        i6 += 1
    if i6 == 10:
        i0 = 'a'
        i1 = 'a'
        i2 = 'a'
        i3 = 'a'
        i4 = 'a'
        i5 = 'a'
        i6 = 'a'
        i7 += 1        

print(k)
print( time.time() - temps )

