import time


ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']

i = 0

k = ''
z = 0
temps = time.time()
op = 0

mdpo = [ 0, 0, 0, 0, 0, 0]

while k != 'enfant':
    k = ma_liste[mdpo [5]] + ma_liste[mdpo [4]] + ma_liste[mdpo [3]] + ma_liste[mdpo [2]] + ma_liste[mdpo [1]] + ma_liste[mdpo [0]]

    if z == 200000:
        print(k)
        z = 0
    z += 1

    mdpo [0] += 1 # On incrémente
    op += 1
    for i in range ( len(mdpo) ):
        if mdpo [i] == 26:
            mdpo [i] = 0
            mdpo [i+1] += 1
        #else : 
            #break
 

print(k)
temps = time.time() - temps
print( temps )
parsec = op/temps
print ( int(parsec), " op par secondes" )

