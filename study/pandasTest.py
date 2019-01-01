#encoding=utf-8
import numpy as np
import pandas as pd

def main():
    s=pd.Series([i*2 for i in range(1,11)])
    print (type(s))
    dates = pd.date_range("20170301",periods=8)
    #index：索引
    df = pd.DataFrame(np.random.randn(8,5),index=dates,columns=list("ABCDE"))
    print(df)

    print(df.head(3))  #前3行
    print(df.tail(3))  #后3行
    print(df.index) #打印索引
    print(df.values) #打印值
    print(df.T)  #转置
    #print(df.sort(columns="C")) #排序,针对C列
    print(df.sort_index(axis=1,ascending=False))  #指定属性  降序
    print(df.describe())  #分析数据

    #Select
    print(type(df["A"])) #选取A的列
    print(df[:3]) #前3行
    print(df["20170301":"20170304"])#按索引区间取

    #通过索引获取
    print(df.loc[dates[0]]) #获取3月1号数据
    print(df.loc["20170301":"20170304",["B","D"]])  #取指定行区间、指定列
    print(df.at[dates[0],"C"])  #取指定值

    #通过下标获取
    print(df.iloc[1:3,2:4])  #获取1-3行  2-4列
    print(df.iloc[1,4])  #第一行，第四列
    print(df.iat[1,4]) #同上

    #选择
    print(df[df.B>0][df.A<0]) #B列大于0  A列小于0
    print(df[df>0]) #只过滤大于0的
    print(df[df["E"].isin([1,2])])  #isin等同于sql中的in

    #SET
    s1=pd.Series(list(range(10,18)),index=pd.date_range("20170301",periods=8))  #新建Series
    df["F"] = s1  #新加一列
    print(df)
    df.at[dates[0],"A"] = 0  #修改索引为0的A列值:0.000000
    print(df)
    df.iat[1,1] = 1 #设置索引第二行，第一列值
    df.ioc[:,"D"] = np.array([4] * len(df))
if __name__ == '__main__':
    main()