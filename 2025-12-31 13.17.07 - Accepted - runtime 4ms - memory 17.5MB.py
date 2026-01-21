class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        # Group indices by value
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        
        min_dist = float('inf')
        
        for num, idx_list in indices.items():
            if len(idx_list) >= 3:
                # Check all consecutive triplets (sorted indices)
                for j in range(len(idx_list) - 2):
                    i, mid, k = idx_list[j], idx_list[j+1], idx_list[j+2]
                    dist = 2 * (k - i)  # Simplified distance formula
                    min_dist = min(min_dist, dist)
        
        return min_dist if min_dist != float('inf') else -1