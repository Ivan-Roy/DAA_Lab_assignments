def search(arr,key):
    count=1
    for i in arr:
        if key==i:
            print("Found after ",count,"comparisons")
            break
        else:
            count+=1

n=int(input())
while n>0:
    arr = list(map(int, input().split()))
    key = int(input())
    search(arr, key)
    n-=1