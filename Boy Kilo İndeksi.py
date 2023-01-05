# Boy Kilo İndeksi

ad= input("Adınız: ")
kilo=float(input("Kilonuz: "))
boy=float(input("Boyunuz: "))

index=(kilo/boy)**2

if(index>=0)and(index<=18.4):
    print("Zayıf")
elif(index>=18.4)and(index<=24.9):
    print("Normal")
elif(index>=24.9)and(index<=29.9):
    print("Kilolu")
elif(index>=29.9)and(index<=34.9):
    print("Şişman(Obez)")
