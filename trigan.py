Matrix=[[-0.5,-2,0,1],[2,2,2,1],[2,0.6,2,1],[4,5,6,0]]
n=4
det=1
for k in range(0, n-1):
    max_s=k
    for i in range(k+1, n):
        if (abs(Matrix[i][k])>abs(Matrix[k][k])):
            max_s=i
        else:
            break
    if(max_s <> k):
        det= det*(-1)
        for j in range(0,n):
            temp=Matrix[k][j]
            Matrix[k][j]=Matrix[max_s][j]
            Matrix[max_s][j]=temp
    if(Matrix[k][k]<>0):
        for i in range(k+1, n):
            coeff=(Matrix[i][k]*1.0)/Matrix[k][k]
            for j in range(0, n):
                    Matrix[i][j]=Matrix[i][j]-coeff*Matrix[k][j]
    else:
        break
print(Matrix)
