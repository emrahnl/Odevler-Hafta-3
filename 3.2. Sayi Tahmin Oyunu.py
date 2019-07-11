##Sayi Tahmin Oyunu
number=81
guess=int(input("Pls guess a number between 0-100: "))
count=1
while number!=guess:
    if number>guess:
        print("Pls try a higher number")
    else:
        print("Pls try a lower number")
    guess=int(input("Pls guess a number between 0-100: "))
    count=count+1
print("You found the number")
print("Number of tries:", count)


                     

          
        
