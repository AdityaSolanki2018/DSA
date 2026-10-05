s = ["h","e","l","l","o"]
s = s[::-1]
print(s)

# Alternative method using two pointers
left, right = 0, len(s) - 1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
print(s)

# Alternative method using recursion
def reverse_string(s, left, right):
    if left >= right:
        return
    s[left], s[right] = s[right], s[left]
    reverse_string(s, left + 1, right - 1)  

reverse_string(s, 0, len(s) - 1)
print(s)