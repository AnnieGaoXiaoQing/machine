#encoding=utf-8
import numpy as np
from keras.models import Sequential  #神经网络容器
from keras.layers import Dense,Activation #Dense：求和层   Activation：激活层
from keras.optimizers import SGD  #SGD随机梯度算法

#
def main():
    #加载数据集
    from sklearn.datasets import  load_iris
    iris = load_iris()
    print(iris["target"])  #目标变量（0,1,2）
    from sklearn.preprocessing import LabelBinarizer
    # 标签化目标变量（0变100，1变010，2变001）
    print(LabelBinarizer.fit_transform(iris["target"],None))  #本行无法运行

    from sklearn.model_selection import train_test_split
    train_data,test_data,train_target,test_target = \
        train_test_split(iris.data,iris.target,test_size=0.2,random_state=1)
    labels_train = LabelBinarizer().fit_transform(train_target)
    labels_test = LabelBinarizer().fit_transform(test_target)
    model = Sequential([
        Dense(5,input_dim=4),  #输入
        Activation("relu"), #激活函数
        Dense(3), #输出
        Activation("sigmoid") #激活函数
    ])

    #模式定义形式二
    #model = Sequential()
    #model.add(Dense(5,input=4))

    #梯度算法优化器 decay:步长 momenttum：实质因子
    sgd = SGD(lr = 0.01,decay=1e-6,momentum=0.9,nesterov=True)
    model.compile(optimizer=sgd,loss="categorical_crossentropy") #指定优化器和损失函数
    model.fit(train_data,labels_train,np_epoch=200,batch_size=40)  #训练200次，每次40数据
    print(model.predict_classes(test_data))
    model.save_weights("./data/w")  #存储结果
    model.loss_weights("./data/w")  #加载结果

if __name__ == '__main__':
    main()