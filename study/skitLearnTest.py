#encoding=utf-8
import os;

def main():
    #数据预处理
    from sklearn.datasets import load_iris
    iris = load_iris();
    print(iris)
    print(len(iris["data"]))
    from sklearn.model_selection import train_test_split   #引入交叉验证
    # 验证集占20%,random_state==1即随机选择30个数据集
    train_data,test_data,train_target,test_target = \
        train_test_split(iris.data,iris.target,test_size=0.2,random_state=1)

    #建模
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(criterion="entropy")  #criterion:信息熵
    clf.fit(train_data,train_target)#建立模型
    y_pred = clf.predict(test_data)#预测

    #验证（准确率和混淆矩阵）
    from sklearn import metrics
    print(metrics.accuracy_score(y_true=test_target,y_pred=y_pred))  #准确率（y_true:真实值，y_pred:预测值）
    print(metrics.confusion_matrix(y_true=test_target,y_pred=y_pred)) #混淆矩阵  横轴实际值，纵轴预测值
    #结果（理想的是对角矩阵，仅对角有值） 1代表预测有问题，真实值是1，预测值是3
    #[[11  0  0]
    #[0 12  1]
    #[0 0  6]]

    #决策树直接输出文件
    with open(os.path.abspath(os.path.dirname(os.getcwd())) + "/data/tree.dot","w") as fw:
        tree.export_graphviz(clf,out_file=fw)

if __name__ == '__main__':
    main()
