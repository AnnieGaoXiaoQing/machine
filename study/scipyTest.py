#encoding=utf-8
import numpy as np


def main():
    from scipy.integrate import quad,dblquad,nquad
    #一元数值积分：结果数值加误差：(1.0000000000000002, 5.842607038578007e-11)
    print("一元积分：")
    print(quad(lambda x:np.exp(-x),0,np.inf))
    print("二元积分：")
    print(dblquad(lambda t,x:np.exp(-x*t)/t**3,0,np.inf,lambda x:1,lambda x:np.inf))
    print("多元积分：")
    def f(x,y):
        return x*y
    def bound_y():
        return [0,0.5]
    def bound_x(y):
        return [0,1-2*y]
    print (nquad(f,[bound_x,bound_y]))

    from scipy import linalg as lg
    arr = np.array([[1,2],[3,4]])
    print("行列式:")
    print(lg.det(arr))
    print("逆矩阵:",lg.inv(arr))
    #解线性方程组
    b=np.array([6,14])
    print("Sol:",lg.solve(arr,b))
    #特征值，特征向量
    print("Eig:")
    print(lg.eig(arr))
    print("LU分解：")
    print(lg.lu(arr))
    print("QR分解：")
    print(lg.qr(arr))
    print("SVD分解：")
    print(lg.svd(arr))
    print("Schur分解：")
    print(lg.schur(arr))

if __name__ == '__main__':
    main()