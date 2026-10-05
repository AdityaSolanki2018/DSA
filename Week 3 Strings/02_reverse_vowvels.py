s = "IceCreAm"
s = list(s)
my_set = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
left = 0
right = len(s) - 1

while left < right:
    if s[left] not in my_set:
        left += 1
    elif s[right] not in my_set:
        right -= 1
    else:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

print(''.join(s))