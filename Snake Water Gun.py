import random
for i in range(1,5):
  x=random.randint(1,3)
  a=int(input("Enter numbers from 1 to 3\n"))
  print("1 is for snake, 2 is for water, 3 is for gun")
  print("Computer chose",x)
  if a==x:
    print("Draw")
  elif a==1 and x==2:
    print("You win")
  elif a==1 and x==3:
    print("AI wins")
  elif a==2 and x==1:
    print("You win")
  elif a==2 and x==3:
    print("AI wins")
  elif a==3 and x==1:
    print("AI wins")
  else:
    print("You win")
    i=i+1
    
