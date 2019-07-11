usernames=[]
try:
   with open("accounts.txt", "r") as file:
      for line in file:
         info = line.split()
         usernames.append(info[0])
except FileNotFoundError:
   pass

username = input("pls enter an username: ")
while username in usernames:
   username = input("pls re-enter an username: ")
   
password = input("pls enter a password: ")

with open("accounts.txt","a") as file:
   file.write(username+" " +password)

print("Congrats! You created your account successfully ")


  


