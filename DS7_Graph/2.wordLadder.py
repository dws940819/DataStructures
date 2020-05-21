'''
    力扣 第1203题：项目管理问题
一、问题描述
    字梯问题：将单词'FOOL'转换为单词'SAGE'。
    前提条件：每一步必须将一个字符转换成另一个字

    举例：FOOL
          POOL
          POLL
          PALE
          SALE
          SAGE
    目的：计算FOOL到SAGE所需要的最小转换次数 
    有的会给定特定的单词列表，比如5000单词量
    将一个字与列表中的每个其他词进行比较O(n^2) 5000^2  =  25000000
    步骤：
    1.将字之间的关系表示成图  (无向图，边未加权)
    2.使用广度优先搜索的图算法来找到从开始字符到结束字的有效路径


         _OOL  F_OL FO_L FOO_
         AOOL  FAOL FOPL FOOA
    实现：用字典实现
    key: _OOL  F_OL FO_L FOO_
    value：对应的单词列表
    {
        '_OOL':[AOOL,...],
        'F_IL':[FAOL,...],
        'FO_L':[FOPL,...],
        'FOO_':[FOOA,...]
    }
'''
from pythonds.graphs import Graph


'''
广(宽)度优先搜索的图算法  (BFS)
    过程：
    1.给定的图G和起始点S，BFS通过探索图中的边找到G中所有的顶点，其中存在从s开始的路径
      找到和s相距为k的所有顶点
      然后找距离为k+1的所有顶点
    特点：BFS先从起始顶点开始添加它的所有的子节点，然后再添加子节点的子节点
    2.怎么确定一个顶点的状态？BFS将每个顶点着色为：白色，灰色和黑色
      所有的顶点被初始化为白色，白色顶点是未发现的顶点
      当一个顶点被发现的时候，它变成灰色：灰色顶点可能有与其相邻的一些白色顶点，表示仍要探索
      当BFS完全探索完一个顶点的时，他就变成黑色：变成黑色意味着这个顶点已经没有与他相邻的白色顶点
    3.使用邻接表示法实现图，使用Queue，存储顶点顺序，决定下一个探索的顶点
      BFS从起始顶点开始，颜色从灰色开始，distance = 0 predecesso = None 表名这个顶点正在被探索。
      BFS的Vertex类拓展版本，中有distance(距离)，predecessor(前导)，color
      把生成的顶点放到队列中，检查队列(迭代邻接表)中前面的顶点中的颜色，如果是白色，顶点未被开发：
      (1)新的，未开发的顶点nbr，被着色为灰色
      (2)nbr的前导被设置为当前节点currentVert
      (3)到nbr的举例设置为到currentVert + 1的距离
      (4) nbr被添加到队列的末尾。


深度优先搜索的图算法
'''
from pythonds.graphs import Graph,Vertex
from pythonds.basic.queue import Queue

# 顶点
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    lines = wfile.readlines()
    for line in lines:
        word = line.strip('\n')
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g


def bsf(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)

    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        # 遍历多有的边
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)

        currentVert.setColor('black')

wordFile = './DS7_Graph/word.txt'
g = buildGraph(wordFile).getVertices()

start = Vertex('FOOL')

print(bsf(g,start))
def traverse(e):
    x = e
    while(x.getPred()):
        print(x.getId())
        x.getPred()
    print(x.getId())

'''
    s:'FOOL'
    相邻点：pool，foil，foul，cool
    队列：-------------------------- 
    rear  cool   foul  foil  pool          front
         --------------------------

         poll (2)
    
    队列：-------------------------- 
    rear   poll   cool foul  foil          front
         --------------------------
         fail (2)
    队列：-------------------------- 
    rear   fail  poll   cool foul          front
         --------------------------
'''