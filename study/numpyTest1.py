#encoding=utf-8
import numpy as np


def main():
    lst=[[1,2,3],[4,5,3]]
    print (type(lst))
    np_list=np.array(lst)
    print (type(np_list))
    np_list = np.array(lst,dtype=np.float)
    print(np_list.shape) #某行某列
    print(np_list.ndim) #维度
    print(np_list.dtype) #类型
    print(np_list.itemsize)

    #some Arrays
    print(np.zeros([2,4]))  #初始化全部为0
    print(np.ones([3,5]))  #初始化全部为1

    print("Rand:")  #随机数（均匀分布）
    print(np.random.rand(2,4))
    #无入参，则仅打印1个
    print(np.random.rand())
    #打印随机整数
    print("RandInt:")
    #前2个参数是范围，第3个参数为数量
    print(np.random.random_integers(1, 10))
    print(np.random.random_integers(1,10,3))
    #正态分布
    print("Randn:")
    print(np.random.randn())
    #限定尺寸
    print(np.random.randn(2,4))
    #随机生成正定列表数
    print("Choice:")
    print(np.random.choice([10,20,30,1,2,3]))
    #beta分布
    print("Distribute:")
    print(np.random.beta(1,10,100))

    #产生等差数列
    print(np.arange(1,11))
    #设置为2行5列（2,5）或（2,-1）
    lst = np.arange(1, 11).reshape(2, -1)
    print(np.exp(lst)) #自然指数
    print(np.exp2(lst)) #指数平方
    print(np.sqrt(lst)) #开方
    print(np.sin(lst)) #sin函数
    print(np.log(lst)) #对数函数

    lst=np.array([[[1,2,3,4],
                   [4,5,6,7]],
                  [[7,8,9,10],
                   [10,11,12,13]],
                  [[14,15,16,17],
                   [18,19,20,21]]
                  ])
    print(lst.sum(axis=1))
    print("Max:")
    print(lst.max(axis=1))
    print("Min:")
    print(lst.min(axis=1))

    lst1 = np.array([10,20,30,40])
    lst2 = np.array([4,3,2,1])

    print("Add:")
    print(lst1 + lst2)
    print("Sub:")
    print(lst1 - lst2)
    print("Mul")
    print(lst1 * lst2)
    print("Div")
    print(lst1/lst2)
    print("Square")
    print(lst1**2)
    #点乘
    print("Dot:")
    print(lst1.reshape([2,2]))
    print(lst2.reshape([2, 2]))
    print(np.dot(lst1.reshape([2,2]),lst2.reshape([2,2])))

    print("Cancatenate")
    print(np.concatenate((lst1,lst2),axis=0))
    print(np.vstack((lst1,lst2)))  #追加并换行
    print(np.hstack((lst1,lst2))) #不换行

    from numpy.linalg import *
    print(np.eye(3))  #单位矩阵
    lst = np.array([[1.,2.],[3.,4.]])

    print("Inv:")  #逆矩阵
    print(inv(lst))
    print("T:") #转置矩阵
    print(lst.transpose())
    print("Det:") #行列式
    print(det(lst))

    print(eig(lst))

    y=np.array([[5.],[7.]])
    print("Solve")
    print(solve(lst,y))

    print("阶跃函数:") #阶跃函数
    print(np.fft.fft(np.array([1,1,1,1,1,1,1,1])))
    print("相关系数:") #相关系数
    print(np.corrcoef([1,0,1],[0,2,1]))
    print("生成一元二次方程:") #生成一元二次方程
    print(np.poly1d([2,1,3]))

if __name__ == "__main__":
    main()