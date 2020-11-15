# NUMBER GUESSİNG APPLİCATİON

import random
import time

print('Sayi tahmin etme oyununa hosgeldiniz! 1-20 arasinda sayi tahmin edin')

sayi = random.randint(1,20)
tahmin_hakki = 3

while True:
    tahmin = int(input('tahmininiz: '))
    
    if tahmin == sayi:
        print('sorgulaniyor')
        time.sleep(1)
        print('Tebrikler, 10 tl kazandiniz')
        break
    elif tahmin > sayi:
        print('sorgulaniyor')
        time.sleep(1)
        tahmin_hakki -=1
        print('Daha kucuk bir sayi tahmin ediniz')
        print('Kalan tahmin hakkınız: ', tahmin_hakki)
    else:
        print('sorgulaniyor')
        time.sleep(1)
        tahmin_hakki -=1
        print('Daha buyuk bir sayi tahmin ediniz')
        print('Kalan tahmin hakkınız: ', tahmin_hakki) 
    if tahmin_hakki == 0:
        print(' GAME OVER!')
        print('Secilen Sayi: ', sayi)
        time.sleep(5)
        break
        