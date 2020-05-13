'''
    顺序查找 - 无序表  O(n)
    顺序查找 - 有序表  O(logn)
    散列              O(1)

    一、什么是散列
        散列表是一种数据的集合，其中的每个数据都是通过某种特定的方式存储以方便日后的查找，散列表中的每个位置叫做槽，能够存放一个数据项，并以从0开始的递增整数命名，某个数据项与在散列表中存储它的槽之间的映射叫做散列函数
        散列函数可以将任意一个数据项存储到集合中并返回一个介于槽命名区间内（0-m-1）的整数
        假设有11个空槽的一个散列 ---------------------------------------------
                               | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
                               ---------------------------------------------
        假设我们又一列整数：54,26,93,17,77,31
        假设设定散列函数为：求余，54%11 4 余10
                               ---------------------------------------------
                               | 77 |  |  |  | 26 | 93 | 17 |  |  | 31 | 54 |
                               ---------------------------------------------

        假设我要查找24这个元素  24%11 = 2余2：查找一个数据项时，只需要使用散列函数去计算得到这个数据项对应槽的名字，并在这个槽中检查该数据项，是否存在即可。

        问题：仅能在每一个数据项在散列中占有不同槽的情况下才能正常运作，比如说再放入44,55，根据求余的散列函数，两个甚至多个数据就需要存储到同一个槽中，这种情况被称为：冲突
    
    二、散列函数

        折叠法：首先将数据分成相同长度的片段（最后一个片段长度可以不等），接着讲这些片段相加，再求余得到其散列值。

        例如：有一串电话号码 436-555-4601 每两个分一个片段：43 65 55 46 01 210%11 余1 槽1

        平方取中法：首先将数据取平方，然后取平方数的某一部分。例如数据项是44,44^2=1936,再取出中间的两位数93，再进行求余 93%11 = 余5

        非数字：cat 怎么存cat这种非数字  =》 通过ASCII转换成数字  a:97 c:99 t:116
        97+99+116 = 312 312%11 = 4

        ASCII转换成数字的散列函数
        def hash(astring,tablesize):
            sum = 0
            for pos in range(len(astring)):
                sum = sum + ord(astring[pos])
            return sum%tablesize
        print(hash('cat'))
'''