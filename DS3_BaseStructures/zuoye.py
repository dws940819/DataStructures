# 1.将下列值通过“除以二”转化为二进制。写出余数的栈。
class Stack:
    def __init__(self):
        self.lst = [None for i in range(30)]
        self.top = -1

    def push(self, data):
        if self.top == len(self.lst) - 1:
            print("栈挤爆了")
        else:
            self.top += 1
            self.lst[self.top] = data

    def pop(self):
        if self.top == -1:
            return None
        else:
            data = self.lst[self.top]
            self.top -= 1
            return data


s = Stack()
data = [17,45,96]
for x in data:
    print(x)
    while x != 0:
        ys = x % 2
        s.push(ys)
        x = x // 2

while s.top != -1:
    print(s.pop(), end='')


