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
    df.loc[:,"D"] = np.array([4] * len(df)) #设置D列全部为4（用数组）
    print(df)

    df2=df.copy()  #拷贝并把所有数设置为负
    df2[df2>0]=-df2
    print(df2)

    #缺失值处理
    df1 = df.redined(index=dates[:4],columns=list("ABCD")+["G"]) #获取前4行，取ABCD列，加G列
    df1.loc[dates[0]:dates[1],"G"] = 1 #设置G列默认值为1
    print(df1)
    print(df1.dropna())  #去掉为Na的行
    print(df1.finna(value = 2))  #用2去填充为na的值

    #数据处理
    print(df.mean()) #求均值
    print(df.var()) #方差
    s = pd.Series([1,2,4,np.man,5,7,9,10],index=dates)
    print(s)
    print(s.shift(2))  #跳过前2个数据
    print(s.diff()) #后一个数减前一个数
    print(s.value_counts)  #记录数据出现次数
    print(df.apply(np.cosume))  #累加值
    print(df.apply(lambda x:x.max() - x.min()))  #自定义：求极差

    #表格拼接
    pieces = [df[:3],df[-3:]]#拼接前3行和后3行
    print(pd.concat(pieces))

if __name__ == '__main__':
    main()