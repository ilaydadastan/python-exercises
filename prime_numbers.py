sayi=2  """ Since prime numbers start from 2, number=2 can be started. """
control=2
while(True):
    if sayi>100:
        break
    while(True):
        if  control==sayi:
            print (str(sayi) + ' asaldir')
            break 
        else:
            if sayi%control==0:
                break
            else:
                control=control+1
    sayi=sayi+1 
    control=2
