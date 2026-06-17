import random 
nombresecret = random.randint(1,100)
tentative=0
Max_tentative=5
print("Guest the Number")
print("devine le nombre entre 1 et 100 ")

 
while tentative < Max_tentative:
    n=int(input("Entrez votre proposition:"))
    tentative +=1
    if n < nombresecret:
        print ("Le nombre est trop petit")
        # Je fait des commit
    elif n > nombresecret:
        print("Le nombre est trop grang")
    else:
        print("Merci! vous avez trouvez le le nombre")
        break
        print("Game Over!")
        print(f"Le nombre est était{nombresecret}")