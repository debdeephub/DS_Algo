class Solution:
    def twoNumSum(self,arr,num):
        l = []

        for i in range(len(arr)-1):
            firstNum = arr[i]
            for j in range(i+1,len(arr)):
                secondNum = arr[j]
                if firstNum+secondNum == num:
                    l+= [firstNum,secondNum]
                    #l+= [[fisrtNum,secondNum]]
        return l

a = [3,5,-4,8,11,1,-1,6,4]
num = 10
print(Solution().twoNumSum(a,num))
