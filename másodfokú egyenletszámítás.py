import math

def f1(label):
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
    


f1("1.feladat")
