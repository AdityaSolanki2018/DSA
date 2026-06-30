# 1796. Second Largest Digit in a String
def secondHighest(self, s: str) -> int:
        largest = -1
        slargest = -1
        for letter in s:
            if 48<=ord(letter)<=57:
                num = int(letter)
                if num>largest:
                    slargest = largest
                    largest = num
                elif num>slargest and num!=largest:
                    slargest = num 
        return slargest

## Remove duplicates from sorted array

    
