class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        fruits_count = {}
        max_fruits = 0
        for right in range(len(fruits)):
            fruits_count[fruits[right]] = fruits_count.get(fruits[right], 0) + 1

            while len(fruits_count) > 2:
                fruits_count[fruits[left]] -= 1

                if fruits_count[fruits[left]] == 0:
                    del fruits_count[fruits[left]]
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits
                
