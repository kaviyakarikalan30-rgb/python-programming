import random
a=random.randint(1,5)
print("Guess value")
atp=[]
for atp in range(1,4):
  b=int(input("Enter the value:"))
  if b==a:
   print ("value matched")
   break
  elif a>b:
   print("value greater")
  elif a<b:
   print("value lesser")
else:
  print("you lost")