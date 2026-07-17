class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            
            # Condition met: Target found
            if nums[mid] == target:
                return mid
            
            # Check if the left half is strictly sorted
            if nums[low] <= nums[mid]:
                # Target lies inside the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
        return -1