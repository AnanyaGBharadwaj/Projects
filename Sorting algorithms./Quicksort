import random
import time
def gen_data(a,n):
    for i in range(n):
        x=random.randint(0,100)
        a.append(x)
def partition(a,left,right):
    key=a[left]
    i=left+1
    j=right
    while True:
        while a[i]<key and i<right:
            i=i+1
        while a[j]>key and j>left:
            j=j-1
        if i<j:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
        else:
            break
    a[j],a[left]=a[left],a[j]
    return j
def quick_sort(a,low,high):
    if low<high:
        k=partition(a,low,high)
        quick_sort(a,low,k-1)
        quick_sort(a,k+1,high)
a=[]
print("Enter size")
n=int(input())
gen_data(a,n)
print("The numbers are:")
print(a)
start=time.time()
quick_sort(a,0,n-1)
end=time.time()
print("The sorted numbers are:")
print(a)
print("Time required to sort:",(end-start))
