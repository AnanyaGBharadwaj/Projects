money=0
name=input("Enter your name")
print("Hello!",name,"\nLet us play a small quiz")
print("Here is your first question")
print("Which is the capital city of Karnataka?")
option1=["1.Mysuru", "2.Bengaluru", "3.Hubli", "4.Kodagu"]
print(option1)
answer1=input("Enter your answer")
if answer1==option1[1]:
    print("Yes, right answer")
    money=money+10000
else:
    print("Sorry, wrong answer it's option 2.Bengaluru")
print("Here is your second question")
print("Who was the first president of Independent India?")
option2=["1.Rajendra Prasad", "2.Jawaharlal Nehru", "3.Sardar Vallabhbhai Patel", "4.Indira Gandhi"]
print(option2)
answer2=input("Enter your answer")
if answer2==option2[0]:
    print("Yes, right answer")
    money=money+10000
else:
    print("Sorry, wrong answer it's option 1.Rajendra Prasad")
print("Great! You completed the quiz")
if money==0:
    print("Sorry! You won nothing. Better luck next time")
else:
    print("Congratulations!You won Rs.",money)
