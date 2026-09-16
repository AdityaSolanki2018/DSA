def fourSumCount(nums1, nums2, nums3, nums4):
        my_map = {}
        count = 0
        for i in nums1:
            for j in nums2:
                if i+j in my_map:
                    my_map[i+j]+=1
                else :
                    my_map[i+j] = 1
        
        for k in nums3:
            for l in nums4:
                if -(k+l) in my_map:
                    count+=my_map[-(k+l)]
        
        return count
