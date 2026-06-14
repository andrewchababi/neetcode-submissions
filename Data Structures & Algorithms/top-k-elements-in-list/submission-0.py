class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        frequency = collections.Counter(nums)
        
        # Step 2: Get the k most common elements
        most_frequent = frequency.most_common(k)
        
        # Step 3: Extract just the elements from the tuples
        return [item for item, count in most_frequent]