'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise. 

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

def isAnagram(s: str, t: str) -> bool:
    if len(s) == len(t):
        my_map = {}
        for letter in s:
            if letter in my_map:
                my_map[letter]+=1
            else:
                my_map[letter] = 1
        
        for i in t:
            if i in my_map and my_map[i]>0 :
                my_map[i] -=1
            else:
                return False
        return True
    else: return False