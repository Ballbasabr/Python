n=int(input("Введите номер месяца: "))

def month_to_season(n):
    if n==1 or n==2 or n==12:
        print("Зима")
    elif n==3 or n==4 or n==5:
        print("Весна")    
    elif n==6 or n==7 or n==8:
        print("Лето")     
    elif n==9 or n==10 or n==11:
        print("Осень")     
    else:
        print("Нет такого месяца") 

month_to_season(n)        