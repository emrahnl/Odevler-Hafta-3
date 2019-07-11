shape=input("Which shape do you want to calculate: ")

if shape=='triangle':
   height=int(input("height: "))
   base=int(input("base: "))
   area=(height*base)/2
   print("area: ",area)

elif shape=="square":
   side=int(input("side: "))
   area=side*side
   print("area: ",area)

elif shape=='rectangle':
   side1=int(input("side1: "))
   side2=int(input("side2: "))
   area=side1*side2
   print("area: ",area)

elif shape=='cube':
   side=int(input("side: "))
   volume=side**3
   print("volume:",volume)

elif shape=="sphere":
   radius=int(input("radius: "))
   volume=(4*3.14*(radius**3))/3
   print("volume:",volume)

elif shape=="cone":
   radius=int(input("radius: "))
   height=int(input("height: "))
   volume = (1/3)*3.14*(radius**2)*height
   print("volume:",volume)
   
else:
   print("invalid shape, please enter a valid shape: ") 
