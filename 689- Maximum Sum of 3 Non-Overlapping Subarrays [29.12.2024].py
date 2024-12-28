class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        sum_k = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        sum_k[0] = current_sum

        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            sum_k[i] = current_sum

        left = [0] * (n - k + 1)
        max_sum = sum_k[0]
        for i in range(1, n - k + 1):
            if sum_k[i] > max_sum:
                max_sum = sum_k[i]
                left[i] = i
            else:
                left[i] = left[i - 1]

        right = [0] * (n - k + 1)
        right[n - k] = n - k
        max_sum = sum_k[n - k]
        for i in range(n - k - 1, -1, -1):
            if sum_k[i] >= max_sum:
                max_sum = sum_k[i]
                right[i] = i
            else:
                right[i] = right[i + 1]

        max_sum = 0
        result = [-1, -1, -1]
        for j in range(k, n - 2 * k + 1):
            i, l = left[j - k], right[j + k]
            total = sum_k[i] + sum_k[j] + sum_k[l]
            if total > max_sum:
                max_sum = total
                result = [i, j, l]

        return result
solution = Solution()
nums1 = [1, 2, 1, 2, 6, 7, 5, 1]
k1 = 2
print(solution.maxSumOfThreeSubarrays(nums1, k1))  # Output: [0, 3, 5]

nums2 = [1, 2, 1, 2, 1, 2, 1, 2, 1]
k2 = 2
print(solution.maxSumOfThreeSubarrays(nums2, k2))  # Output: [0, 2, 4]
