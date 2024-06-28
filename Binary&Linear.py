# find 2nd largest using linear search
# find 13 using Binary

#1:
arr = [1,4,7,9,5,3,4,7,5,10,4,7]
largest = arr[0]
second = 0
for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i < largest:
        second = i

print(second)

# 2:
def binary_search(a, target):
    a = sorted(a)
    print(a)
    lower = 0
    upper = len(a)-1
    while lower <= upper:
        mid = (upper+lower)//2
        if a[mid] == target:
             return mid
        else:
            if a[mid] < target:
                lower = mid+ 1
            else :
                upper = mid-1
    return 'Not Found'

a = [1,2,5,7,9,7,45,3,2,5,6,13,2,3,4,6,77,8]
print(binary_search(a, 6))