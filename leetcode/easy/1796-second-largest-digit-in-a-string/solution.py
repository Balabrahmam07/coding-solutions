class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second = -1
        for i in s:
            if not i.isalpha():
                n = int(i)
                if n > largest:
                    second = largest
                    largest = n
                elif largest > n > second:
                    second = n
                
        return second
