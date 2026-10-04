from collections import Counter
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        fruits = Counter(fruits)
        n = fruits.most_common(1)[0][1]
        x = fruits.most_common(2)[1][1]
        return n+x