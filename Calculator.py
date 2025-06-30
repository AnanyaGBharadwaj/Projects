a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=input("Choose any operation")
if c=='+':
    c=a+b
elif c=='-':
    c=a-b
elif c=='*':
    c=a*b
elif c=='/':
    c=a/b
elif c=='%':
    c=int(a)/int(b)
print(c)
