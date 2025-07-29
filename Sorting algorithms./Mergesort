import random
def gen_data(a,n):
    for i in range(n):
        x=random.randint(0,100)
        a.append(x)
def merge_sort(a,low,high):
    if high-low<1:
        return
    mid=int((high+low)/2)
    merge_sort(a,low,mid)
    merge_sort(a,mid+1,high)
    merge(a,low,mid,high)
def merge(a,low,mid,high):
    k=low
    i=0
    j=0
    left=a[low:mid+1]
    right=a[mid+1:high+1]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            a[k]=left[i]
            i=i+1
        else:
            a[k]=right[j]
            j=j+1
        k=k+1
    if i<len(left):
        while i<len(left):
            a[k]=left[i]
            i=i+1
            k=k+1
    else:
        while j<len(right):
            a[k]=right[j]
            j=j+1
            k=k+1
a=[]
print("Enter size")
n=int(input())
gen_data(a,n)
print("The numbers are:")
print(a)
merge_sort(a,0,n)
print("The sorted numbers are:")
print(a)
