class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l1=[]
        for i in range(len(accounts)):
            c=0
            for j in range(len(accounts[i])):
                c+=accounts[i][j]
            l1.append(c)
        return max(l1)
