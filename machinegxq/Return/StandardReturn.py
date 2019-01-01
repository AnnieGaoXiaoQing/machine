from numpyTest import *
import matplotlib.pyplot as plt
#-*- coding: utf-8 -+-

def loadDatSet(filename):
    numFeat = len(open(filename).readline().split('\t'))-1
    dataMat=[]; labelMat=[]
    fr=open(filename)
    for line in fr.readlines():
        lineArr=[]
        curLine=line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

def standRegres(xArr,yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws

if __name__ == '__main__':
    xArr,yArr=loadDatSet('ex0.txt')
    ws = standRegres(xArr,yArr)
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = xMat*ws
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten.A[0])
    xcopy = xMat.copy()
    xcopy.sort(0)
    yHat = xcopy*ws
    ax.plot(xcopy[:,1],yHat)
    plt.show()