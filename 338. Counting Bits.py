class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        '''
        Solution 1: Formula based.
        The number of 1's in a binary number is given by 
        sum of value at index [whole dividing the number by 2(base)] and modulo of the 2(base).
        (i%2)The idea is binary even numbers will always have odd number of 1's, similarly for bin odd no -> even no of 1's. 
        
        
        ''' 
        ans=[0]
        for i in range(1,n+1):
            ans.append(ans[i//2]+i%2)
        return ans