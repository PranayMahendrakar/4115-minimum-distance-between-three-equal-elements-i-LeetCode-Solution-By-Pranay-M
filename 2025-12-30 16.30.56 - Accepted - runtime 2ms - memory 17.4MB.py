class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        
        min_dist = float('inf')
        for idx_list in indices.values():
            if len(idx_list) >= 3:
                # For consecutive indices i, j, k: distance = 2*(k-i)
                for i in range(len(idx_list) - 2):
                    dist = 2 * (idx_list[i+2] - idx_list[i])
                    min_dist = min(min_dist, dist)
        
        return min_dist if min_dist != float('inf') else -1