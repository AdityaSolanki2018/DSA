def canConstruct(ransomNote: str, magazine: str) -> bool:
        my_map={}
        for char in magazine:
            if char in my_map:
                my_map[char]+=1
            else:
                my_map[char] = 1
        
        for letter in ransomNote:
            if letter in my_map and my_map[letter]>0:
                my_map[letter]-=1
            else: return False
        
        return True