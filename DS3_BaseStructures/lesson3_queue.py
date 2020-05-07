'''
    队列：是一系列有顺序的元素集合，新元素加入在队列的一端，这一端叫做“队尾”
        已有元素的移出发生在队列的另一端，叫做“对首（front）”，当一个元素被加入到队列之后，它就从队尾向对首前进，直到它成为下一个即将被移出队列的元素
    先进先出（FIFO）：最新被加入的元素处于队尾，在队列中停留最长时间的元素处于队首


    抽象数据类型（ADT）：
        Queue（）创建一个空队列对象，无需参数，返回空的队列
        enqueue(item) 将数据项添加到队尾，无返回值
        dequeue() 从队首移出数据项，无需参数，返回值为队首数据项
        isEmpty() 是否队列为空，无需参数，返回值为布尔值
        size（） 返回队列中的数据项的个数，无需参数


    用python list实现队列
    队尾在列表的位置
    enqueue    insert()  O(n)
    dequeue    pop()     O(1)

'''

# class Queue():

#     def __init__(self):
#         self.items = []

#     def enqueue(self,item):
#         self.items.insert(0,item)
    
#     def dequeue(self):
#         return self.items.pop()

#     def isEmpty(self):
#         return self.items == []
    
#     def size(self):
#         return len(self.items)

# q = Queue()
# q.enqueue(6)

# q.enqueue('cat')
# q.enqueue(False)
# print(q.size())
# print(q.isEmpty())
# q.dequeue()

'''
    马铃薯游戏（击鼓传花）选定一个人作为开始的人，数到num个人，将此人淘汰
'''
from pythonds.basic.queue import Queue

name_list = ['嬴政','刘邦','项羽','刘备','刘彻','李世民','赵匡胤','朱元璋','朱棣','乾隆']
num = 4

def send_flower(name_list,num):
    q = Queue()
    for name in name_list:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        n = q.dequeue()
        print(n)
    return q.dequeue()

print(send_flower(name_list,num))




'''
    模拟打印机

    平均每天任意一个小时有大约10个学生在实验室里，在这一小时中通常每人发起2次打印任务，每个打印任务的页数从1到20页不等，实验室中的打印机老旧，如果以草稿模式打印，每分钟可以打印10页;打印机可以转换完成高品质的打印模式，但每分钟只能打印5页，较慢的打印速度可能会使学生等待太长的时间，应该采用哪种打印模式？
'''


