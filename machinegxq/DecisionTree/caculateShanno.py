# -*- coding:utf-8 -*-
from math import log
import operator

#样本数据及对应特征
def createData():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

#香农熵
def calcShannoEnt(dataSet):
    numEntries = len(dataSet)   #样本集个数
    labelCounts = {}            #存放类型对应样本数
    for featVec in dataSet:
        currentLabel = featVec[-1]  #获取单个样本数据
        if currentLabel not in labelCounts.keys(): #若集合中不存在此类样本结果，先初始化，再加1
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries  #每种类型占总数比例
        shannonEnt -= prob * log(prob,2) #计算香农熵
    return shannonEnt  #返回熵结果

#按照特征划分数据集
#axis：特征所在列数（0…）  value：特定具体值
def splitDataSet(dataSet, axis, value):
    retDataSet =[]  #定义List
    for featVec in dataSet:
        if featVec[axis] == value:  #所选特征列等于传来的特征值
            reduceFeatVec = featVec[:axis]   #获取样本数据指定列的数（初始化）
            reduceFeatVec.extend(featVec[axis+1:]) #获取指定特征列后面的特征和目标变量[1, 'no']
            retDataSet.append(reduceFeatVec) #添加到集合中
    return retDataSet #[[1, 'no'], [1, 'no']]

#选取最好的特征值
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) -1 #获取特征列数
    baseEntropy = calcShannoEnt(dataSet)  #初始化数据集香农熵
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):  #遍历特征
        featList = [example[i] for example in dataSet] #获取指定列数据集
        uniqueVals = set(featList) #特征数据去重[0,1]
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)  #获取切分特征后的数据
            prob = len(subDataSet)/float(len(dataSet))  #切分后特征所占比例
            newEntropy += prob * calcShannoEnt(subDataSet)  #计算信息增益
        infoGain = baseEntropy - newEntropy  #计算信息增益
        if(infoGain > bestInfoGain): #？？直接计算两个特征的信息增益比较可以不
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys() : classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),
        key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


#创建树的函数
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]    #获取最后一列数据
    if classList.count(classList[0]) == len(classList): #所有样本同一类型情况
        return classList[0]
    if (dataSet[0]) == 1:  #只有一条样本数据时
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet) #选择最好的特征
    bestFeatLabel = labels[bestFeat] #获取特征标签
    myTree = {bestFeatLabel:{}} #为特征标签初始化列表
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet] #获取最优特征列数据
    uniqueVals = set(featValues) #数据去重
    for value in uniqueVals: #遍历特征
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree #{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}

if __name__ == '__main__':
    dataSet,labels = createData();
    #shannonEnt = calcShannoEnt(dataSet)
    #splitDataSet(dataSet,0,0)
    #print chooseBestFeatureToSplit(dataSet)
    print createTree(dataSet,labels)


