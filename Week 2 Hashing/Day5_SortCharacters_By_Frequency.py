'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
'''

# Hashing + Bucket Sort
from collections import defaultdict
def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for char in s:
            d[char]+=1
        arr = [set() for _ in range(len(s)+1)]
        for key,value in d.items():
            arr[value].add(key)

        ans = ""
        i = len(arr)-1
        while(i>=0):
            if arr[i] != set():
                ans = ans + (arr[i].pop())*i
            else:
                i-=1
        return ans

# Highly Optimized Solution
from collections import Counter
def frequencySort(self, s: str) -> str:
        # Count frequency of each character
        counts = Counter(s)
        
        # Build string by repeating each character by its count in descending order
        return "".join(char * count for char, count in counts.most_common())