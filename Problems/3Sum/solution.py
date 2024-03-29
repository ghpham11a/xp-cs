class Solution(object):

    def three_sum(self, nums):
        
        output = []

        nums.sort()

        for index, num in enumerate(nums):

            if index > 0 and num == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:

                three_sum = num + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    output.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return output

solution = Solution()

assert(solution.three_sum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])

print("PASS")