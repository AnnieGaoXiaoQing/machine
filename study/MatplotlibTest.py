#encoding=utf-8
import numpy as np

def main():
    import matplotlib.pyplot as plt
    x = np.linspace(-np.pi,np.pi,256,endpoint=True)  #定义横轴
    c,s = np.cos(x),np.sin(x) #定义余弦函数和正弦函数
    plt.figure(1)  #指定图
    plt.plot(x,c,color="blue",linewidth=1.0,linestyle="-",label="COS",alpha=0.5) #余弦  颜色、线宽、标示
    plt.plot(x,s,"r*",label="SIN")  # 正弦
    plt.title("COS & SIN")
    ax=plt.gca()  #获取图形边界
    ax.spines["right"].set_color("none")  #隐藏右边界
    ax.spines["top"].set_color("none") #隐藏顶部边界
    ax.spines["left"].set_position(("data",0))  #左轴位置设置到0处
    ax.spines["bottom"].set_position(("data",0))  #底部轴位置设置到0处
    ax.xaxis.set_ticks_position("bottom")  #???
    ax.yaxis.set_ticks_position("left") #???
    plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],   #设置x轴数组角度表示
               [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$','$+\pi$']) #数组1：x轴的位置 数组2：x轴的内容
    plt.yticks(np.linspace(-1,1,5,endpoint=True)) #设置y轴数值间距
    for label in ax.get_xticklabels() + ax.get_yticklabels():  #设置标签
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor="white",edgecolor="None",alpha=0.2))
    plt.legend(loc="upper left") #图例
    plt.grid() #网格线
    #plt.axis([-1,1,-0.5,1])  #指定范围
    plt.fill_between(x,np.abs(x)<0.5,c,c<0.5,color="green",alpha=0.25)  #颜色填充
    t=1 #1地方设置
    plt.plot([t,t],[0,np.cos(t)],"y",linewidth=3,linestyle="--")  #加线
    plt.annotate("cos(1)",xy=(t,np.cos(1)),xycoords="data",xytext=(+10,+30),
                   textcoords="offset points",arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2")) #加注释
    plt.show()



if __name__ == '__main__':
    main()