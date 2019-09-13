"""
使用栈实现队列的下列操作：
push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # if len(self.output) is not 0:
        #     self.output.pop()
        # else:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            return None
        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.input) == 0 and len(self.output) == 0

# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':

    obj = MyQueue()
    obj.push(3)
    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.peek()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)
