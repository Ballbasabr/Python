

#def bank(X, Y):
   # for _ in  range(Y):
    #    X += X * 0.10 
    #return X
def bank(X, Y):
    
    if Y == 0:
        return X
    else:
        return bank(X * 1.10, Y - 1)

deposit = int(input("Cколько вы хотите положить рубле на счёт под 10 % годовых ? "))
years = int(input("На сколько лет? "))


final_amount = bank(deposit, years)
print("Сумма на счету спустя", years, "лет:", final_amount, "рублей")