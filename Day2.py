# Second Largest number in an array
def second_largest(arr:list)->int:
    largest = 0
    secondlargest = 0
    for i in range(len(arr)):
        if arr[i]> largest:
            secondlargest = largest
            largest = arr[i]
        elif arr[i]> secondlargest and arr[i]!=largest:
            secondlargest = arr[i]
    return secondlargest

arr = [1, 2, 3, 4, 5]
print(second_largest(arr))
