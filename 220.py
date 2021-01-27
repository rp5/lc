class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        def check(bkt, i, n):
            if bkt not in bktMap:
                return False
            idx, val = bktMap[bkt]
            if abs(idx - i) <= k and abs(val - n) <= t:
                return True
            return False
        
        bktMap = {}
        for i, n in enumerate(nums):
            bkt = n // (t+1)
            # checks current, prev and next bucket
            for b in [bkt, bkt+1, bkt-1]:
                if check(b, i, n):
                    return True
            bktMap[bkt] = (i, n)  
        return False
