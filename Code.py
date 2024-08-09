class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        answer = prices[:]
        
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                answer[idx] -= prices[i]
            stack.append(i)
        
        return answer
