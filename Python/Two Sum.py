
class Solution(object):
    def twoSum(self, nums, target):
        result = []
        hashtable = {}
        for i in xrange(len(nums)):
            x = nums[i]
            if target - x in hashtable:
                result = [hashtable[target-x]+1, i+1]
                return result
            else:
                hashtable[x] = i
        return result

if __name__ == '__main__':
    num1 = [0,4,3,0]
    target1 = 0
    so1 = Solution()
    res1 = so1.twoSum(num1, target1)
    print res1