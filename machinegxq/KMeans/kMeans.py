#!/usr/bin/python
# -*- coding: utf-8 -*-
from numpyTest import*

#加载数据
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        ftlLine = map(float,curLine)  #数据初始化float类型
        dataMat.append(ftlLine)
    return dataMat

#欧式距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA -vecB,2)))
    # power 样本点平方（(x1-x2)^2+(y1-y2)^2）
    # sqrt 求和后开方

#构建k个随机质心
def randCent(dataSet, k):
    n = shape(dataSet)[1]         #获得列数
    centroids = mat(zeros((k,n))) #k行n列的零阶矩阵
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)
    return centroids


#Kmeans2
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]  #样本数
    clusterAssment = mat(zeros((m,2))) #获得m*2矩阵（一列簇分类结果，一列误差）
    centroids = createCent(dataSet,k)  #初始化K个质心
    clusterChanged = True #簇更改标记
    while clusterChanged:
        clusterChanged = False
        #样本点加入到最近的簇
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
            #更新簇
            for cent in range(k):
                if clusterAssment[i, 0] != minIndex: clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist ** 2
        return centroids, clusterAssment

# 二分K均值
# k:簇个数   distMeas：距离生成器
def biKmeans(dataSet, k, distMeas=distEclud):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList =[centroid0] #create a list with one centroid
    for j in range(m):#calc initial Error
        clusterAssment[j,1] = distMeas(mat(centroid0), dataSet[j,:])**2
    while (len(centList) < k):
        lowestSSE = inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A==i)[0],:]#get the data points currently in cluster i
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
            sseSplit = sum(splitClustAss[:,1])#compare the SSE to the currrent minimum
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:,0].A!=i)[0],1])
            print "sseSplit, and notSplit: ",sseSplit,sseNotSplit
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList) #change 1 to 3,4, or whatever
        bestClustAss[nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentToSplit
        print 'the bestCentToSplit is: ',bestCentToSplit
        print 'the len of bestClustAss is: ', len(bestClustAss)
        centList[bestCentToSplit] = bestNewCents[0,:].tolist()[0]#replace a centroid with two best centroids
        centList.append(bestNewCents[1,:].tolist()[0])
        clusterAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:]= bestClustAss#reassign new clusters, and SSE
    return mat(centList), clusterAssment;

if __name__=="__main__":
    dataMat = loadDataSet('testSet.txt')
    randCent(mat(dataMat), 3)
    #kMeans(mat(dataMat),3,distEclud,randCent)
    #biKmeans(mat(dataMat),3,distEclud)





