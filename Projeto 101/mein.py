import random

response = "y"
while response == "y":
    n = random.randint(1,6)
    if n == 1:
        print("-----")
        print("     ")
        print("--1--")
        print("     ")
        print("-----")
    if n == 2:
        print("-----")
        print("     ")
        print("--2--")
        print("     ")
        print("-----")
    if n == 3: 
        print("-----")
        print("     ")
        print("--3--")
        print("     ")
        print("-----")
    if n == 4:
        print("-----")
        print("     ")
        print("--4--")
        print("     ")
        print("-----")
    if n == 5: 
        print("-----")
        print("     ")
        print("--5--")
        print("     ")
        print("-----")
    if n == 6:
        print("-----")
        print("     ")
        print("--6--")
        print("     ")
        print("-----")
    
    response = input("Pressione y para jogar novamente ou n para sair   ")
    print("\n")
    