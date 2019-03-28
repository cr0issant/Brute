import time


ma_liste = ['0', '1', '2', '3', '4', '5', '6','7','8','9']

i0 = 0
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0

k = ''
z = 0
temps = time.time()
op = 0

while k != '66486670':
    #print(ma_liste[i],ma_liste[j])
    k = ma_liste[i7] + ma_liste[i6] + ma_liste[i5] + ma_liste[i4] + ma_liste[i3] + ma_liste[i2] + ma_liste[i1] + ma_liste[i0]
    if z == 100000:
        print(k)
        z = 0
    z += 1
    op += 1
    i0 += 1 # On incrémente i1
    if i0 == 10:
        i0 = 0
        i1 += 1
    if i1 == 10:
        i0 = 0
        i1 = 0
        i2 += 1
    if i2 == 10:
        i0 = 0
        i1 = 0
        i2 = 0
        i3 += 1
    if i3 == 10:
        i0 = 0
        i1 = 0
        i2 = 0
        i3 = 0
        i4 += 1
    if i4 == 10:
        i0 = 0
        i1 = 0
        i2 = 0
        i3 = 0
        i4 = 0
        i5 += 1
    if i4 == 10:
        i0 = 0
        i1 = 0
        i2 = 0
        i3 = 0
        i4 = 0
        i5 += 1
    if i5 == 10:
        i0 = 0
        i1 = 0
        i2 = 0
        i3 = 0
        i4 = 0
        i5 = 0
        i6 += 1
    if i6 == 10:
        i0 = 0
        i1 = 0
        i2 = 0
        i3 = 0
        i4 = 0
        i5 = 0
        i6 = 0
        i7 += 1        


print(k)
temps = time.time() - temps
print( temps )
parsec = op/temps
print ( int(parsec), " op par secondes" )

