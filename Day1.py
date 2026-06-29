# Linear Search - Find Maximum element

def max_element(arr:list)->int:
    max = 0
    for element in arr:
        if element>max:
            max = element
    return max, arr.index(max)          # O(n) time complexity

arr = [1]
print(max_element(arr))
