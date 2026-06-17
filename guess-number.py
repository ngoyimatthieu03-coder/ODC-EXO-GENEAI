import random 
nombresecret = random.randint(1,100)
tentative=0
Max_tentative=5
print("Guest the Number")
print("devine le nombre entre 1 et 100 ")

 #ceci est une boucle
while tentative < Max_tentative:
<<<<<<< HEAD
    n=int(input("Monsieur ou medame Entrez votre proposition:"))
=======
    n=int(input("Monsieur - medame Entrez votre proposition:"))
>>>>>>> Branch-1
    tentative +=1
    if n < nombresecret:
        print ("Le nombre est trop petit")
        # Je fait des commit
    elif n > nombresecret:
<<<<<<< HEAD
        print("Le nombre est trop grang")
    else:
        print("Monsieur ou Medame Merci! vous avez trouvez le le nombre")
        break
        print("Game Over!")
        print(f"Le nombre est était{nombresecret}")
=======
        print("Le nombre est trop grang est")
    else:
        print("Monsieur ou Medame Merci! vous avez trouvez le le nombre")
        break
        
        print(f"Le nombre est était{nombresecret}")
        # ceci est la fin du cboucle while
>>>>>>> Branch-1
