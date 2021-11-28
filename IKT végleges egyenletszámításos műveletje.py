import math

def valasztas():
    print("Ez egy olyan program amelyben egyenleteket oldhat meg: Első- és másodfokút.")
    print("\tElsőfokú egyenlet: 1.")
    print("\tMásodfokú egyenlet: 2.")
    x = input("Kérem a választásodat; 1, 2: ")
    if (x == "1"):
        elsofoku("Elsőfokú egyenletszámítás: a *x +b=0 formájút oldok meg.")
    elif (x == "2"):
        masodfoku("Másodfokú egyenletszámítás: a*(x*x) + b*x + c = 0")
    else :
        print("Nincs ilyen menüpont.")
    
def elsofoku(label):
    print(label)
    a = float(input("Add meg az a együtthatót:"))
    b = float(input("Add meg a b együtthatót:"))

    if a != 0:
        x = (-b/a)
        print ("Megoldás: " + str(x))
    else:
        if b != 0:
            print("Ennek az egyenletnek nincs megoldása!")
        else:
            print("Ennek az egyenletnek az összes valós szám a megoldása.")
        

def masodfoku(label):
    print(label)
    a = float(input("Kérem az a együtthatót:"))
    b = float(input("Kérek egy b együtthatót:"))
    c = float(input("Kérek egy c együtthatót:"))
    delta = b*b - 4*a*c
    #if delta ==0:
        #print("Ennek az egyenletnek egy megoldása van.")
    if (a == 0):
        if b != 0:
            x = (-c/b)
            print ("Megoldás: " + str(x))
        else:
            if c != 0:
                print("Ennek az egyenletnek nincs megoldása!")
            else:
                print("Ennek az egyenletnek az összes valós szám a megoldása.")
    else:
        if delta < 0:
            print("Ennek az egyenletnek nincs megoldása.")
        elif delta== 0:
            print("A megoldás: ", -b/
                  (2*a))
        else:
            print("Ennek az egyenletnek két megoldása van.")
            if (delta>0):
                 x1 = (-1 * b + math.sqrt(delta))/(2*a)
                 x2 = (-1 * b - math.sqrt(delta))/(2*a)
                 print("Ax x1, x2 számok: %d %d" % (x1, x2))

valasztas()
