class Solution:
    # Go through each number in the array, (decimal) divide it by 10 at each iteration till it's 0
    # So we get the number of digits(c), check if number of digits are divisible by 2. 
    # If so, increment the even digits counter(k) by 1.
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        k=0
        for i in nums:
            num=i
            while(num>0):
                num=num//10
                c=c+1
            if(c%2==0):
                k=k+1
            c=0
        
        return k
    
    # Another Solution 1
    # Check if the number is between the even digits number
        k=0
        for i in nums: 
            if(i>=10 and i<=99):
                k=k+1
            elif(i>=1000 and i<=9999):
                k=k+1
            elif(i>=100000 and i<=999999):
                k=k+1
        
        return k
    
        
    #Another Solution 2
    # Converting the number into string and checking the length of the string is divisible by 2
    # If so, it's an even number.
        k=0
        for i in range(len(nums)):
            if(len(str(nums[i])) % 2 == 0):
                k=k+1
                
        return k
                
            