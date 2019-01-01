# -*- coding:utf-8 -*-
from numpy import *
import operator

#初始化数据
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

#
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]   #数据集大小
    #1、计算距离
    diffMat = tile(inX, (dataSetSize,1)) - dataSet   #将待测点初始化与样本数据的差值
    sqDiffMat = diffMat**2  #差值取平分（欧式距离）
    sqDistances = sqDiffMat.sum(axis=1) #行向量相加
    distances = sqDistances **0.5  #距离开方
    sortedDistIndices = distances.argsort() #将距离排序，获取其由近到远的索引
    #2、#获取距离近数据k个点
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]  #获取相应的目标变量值
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 #统计该类型出现次数
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse = True) #降序
    return sortedClassCount[0][0] #比例最大类型

if __name__=="__main__":
   group,labels = createDataSet()
   print classify0([0,0],group,labels,3)



