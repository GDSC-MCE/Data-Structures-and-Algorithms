
class Solution(object):
    def swapNodes(self, head, k):

        '''
        Solution 1:
        Keep two points, k1 and k2
        let n be the number of nodes that has been traversed
        if(n<k) : only move the first pointer k1, so for k=2, k1 will be moved twice provided n starts at 0
        if(n>k): only move pointer k2, if n>k, once the first pointer is set,
        the second pointer will start it's movement, so it lags k steps till the end of the linked list
        '''
        
        #k2
        #k1
        
        k1 = head
        k2 = head
        node = head
        n=0
        while(node):
            n+=1
            if(n<k):
                k1 = k1.next
            if(n>k):
                k2 = k2.next
            node = node.next
        
        k1.val,k2.val = k2.val,k1.val
        
        return head
                
        
            
        
        
        
        
            
        