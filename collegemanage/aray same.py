#Back-end complete function Template for Python 3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N): 
      
        #using a Map to store frequency of elements.
        mp = {}
        
        #incrementing frequencies of elements present in first array in the Map.
        for i in range (N):
            if A[i] in mp.keys ():
                mp[A[i]] += 1
            else:
                mp[A[i]] = 1
        
        #decrementing frequencies of elements present in second array in the Map.        
        for i in range (N):
            if B[i] not in mp.keys ():
                return False
            mp[B[i]] -= 1
        
        for i in mp.keys ():
            #if frequency of any element in Map now is not zero it means that its 
            #count in two arrays was not equal so the arrays are not equal.
            if mp[i] != 0:
                #returning false since arrays are not equal.
                return False
                
        #returning true if arrays are equal.
        return True