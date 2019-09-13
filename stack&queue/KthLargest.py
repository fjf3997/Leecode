"""
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，
它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
"""


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums)-self.k]


if __name__ == '__main__':
    k = 3
    arr = [4, 5, 8, 2]
    kthLargest = KthLargest(3, arr)
    kthLargest.add(3)
    kthLargest.add(5)
    kthLargest.add(10)
    kthLargest.add(9)
    ret = kthLargest.add(4)
    print(ret)
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)