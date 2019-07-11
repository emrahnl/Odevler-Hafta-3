number=int(input("Pls write a number :"))
is_prime = True
for x in range(2,number):
    if number % x == 0:
        is_prime = False

if is_prime == True:
    print('it is a prime number')
else:
    print('it is not a prime number')

