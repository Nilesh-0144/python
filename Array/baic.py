arr=[1,2,34,45,4]
for i in arr:
    print(i)
print(sum(arr))
print(max(arr))
print(min(arr))
count=0
s=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count+=1
    else:
        s+=1
print("odd:",s)
print("even",count)
print("reverse",arr[::-1])