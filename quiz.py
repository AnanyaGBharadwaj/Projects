print("Hello, Let us play a small quiz")
print("Here is your first question")
print("Which is the capital city of Karnataka?")
print("1.Mysuru, 2.Bengaluru, 3.Hubli, 4.Kodagu")
answer1=input("Enter your answer")
if answer1=="2.Bengaluru":
    print("Yes, right answer")
else:
    print("Sorry, wrong answer it's option 2.Bengaluru")
print("Here is your second question")
print("Who was the first president of Independent India?")
print("1.Rajendra Prasad, 2.Jawaharlal Nehru, 3.Sardar Vallabhbhai Patel, 4.Indira Gandhi")
answer2=input("Enter your answer")
if answer2=="1.Rajendra Prasad":
    print("Yes, right answer")
else:
    print("Sorry, wrong answer it's option 1.Rajendra Prasad")
print("Great! You completed the quiz")
if answer1=="2.Bengaluru" and answer2=="1.Rajendra Prasad":
    print("Congratulations! You won Rs.20,000")
elif answer1=="2.Bengaluru" or answer2=="1.Rajendra Prasad":
    print("Good job! You won Rs.10,000")
else:
    print("Sorry! You won nothing. Better luck next time")
