arr = [1, 3, 5, 7, 7]

m = max(arr)
while m in arr:
    arr.remove(m)

print(max(arr))
