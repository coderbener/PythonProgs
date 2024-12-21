class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i,j=0,0
        counti=0
        countj=0
        ln=len(nums)
        while(i<ln-1):
            if nums[i]<=nums[i+1]:
                counti+=1
            i+=1
        while(j<ln-1):
            if nums[j]>=nums[j+1]:
                countj+=1
            j+=1
        if counti==ln-1 or countj==ln-1:
            return True
        else:
            return False


        