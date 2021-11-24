import math

def elsofoku(label):
    print(label)
    a = float(input("Add meg az a együtthatót:"))
    b = float(input("Add meg a b együtthatót:"))

    if a != 0:
        x = (b/a)
        print ("\tMegoldás: " + str(x))
    else:
        if b != 0:
            print("\t Nincs megoldás!")
        

def masodfoku(label):
    print(label)
    a = float(input("Kérem az a együtthatót:"))
    b = float(input("Kérek egy b együtthatót:"))
    c = float(input("Kérek egy c együtthatót:"))
    delta = b*b - 4*a*c
    if delta ==0:
        print("Az egyenletnek egy megoldása van.")
    else:
        if delta < 0:
            print("Az egyenletnek nincs megoldása.")
        else:
            print("Az egyenletnek két megoldása van.")
    if delta>0:
         x1 = (-1 * b + math.sqrt(delta))/(2*a)
         x2 = (-1 * b - math.sqrt(delta))/(2*a)
         print("Ax x1, x2 számok: %d %d" % (x1, x2))
    

elsofoku("1.feladat: Elsőfokú számítás:")
masodfoku("2.feladat: Másodfokú számítás")
