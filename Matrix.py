class Matrix():
	def __init__(self, lists):
		assert(lists), "This is empty list from initialization matrix"
		self.__matrix=lists.copy()
		self.__rowCount=len(self.__matrix)
		self.__columnCount= len(self.__matrix[0])
		for i in range(len(self.__matrix)):
			assert (len(self.__matrix[i]) == self.__columnCount), "Not rectangular matrix"

	def __add__(self,other):
		assert((self.__rowCount==other.__rowCount) and (self.__columnCount==other.__columnCount)), " Dimension Error from Sum operation"
		return Matrix(list(map(lambda a,b: list(map( lambda c,d : c+d ,a,b)), self.__matrix, other.__matrix)))

	def __sub__(self, other):
		assert((self.__rowCount==other.__rowCount) and (self.__columnCount==other.__columnCount)), " Dimension Error from Sub operation"
		return Matrix(list(map(lambda a,b: list(map( lambda c,d : c-d ,a,b)), self.__matrix, other.__matrix)))

	def __str__(self):
		stringMatrix=""
		for i in range(self.__rowCount):
			for j in range(self.__columnCount):
				stringMatrix+=str(self.__matrix[i][j]) + " "
			stringMatrix+=" \n"
		return stringMatrix


	def __mul__(self,other):
		assert isinstance(other,(int,float)) or isinstance(other, Matrix), "This is not matrixs or , Matrix and Scalar"
		if isinstance(other, Matrix) :
			return self.__matrixMul(other)
		elif isinstance(other,(int,float)):
			return self.__scalarMul(other)

	def __truediv__(self, other):
		return self.__scalarMul(1.0/other)


	def __scalarMul(self,other):
		return Matrix(list(map(lambda x: list(map(lambda y: y*other ,x)), self.__matrix)))

	def __matrixMul(self,other):
		__mat=[]
		assert self.__columnCount==other.__rowCount, "Dimension Error!"
		for row in self.__matrix:
			__rowM=[]
			for col in other.transpose().__matrix:
				__sumM=0
				for x in range(len(col)):
					__sumM+=row[x]*col[x]
				__rowM.append(__sumM)
			__mat.append(__rowM)
		return Matrix(__mat)


	def __pow__(self, N):
		temp=self
		for i in range(N-1): temp=temp*self
		return temp


	def getMatrixInList(self):
		return self.__matrix

	def addRow(self, matrixRow):
		self.__matrix.append(matrixRow.__matrix[0])
		self.__rowCount+=1

	def addColumn(self,matrixCollumn):
		list(map(lambda x, y: x.append(y[0]),self.__matrix, matrixCollumn.__matrix))
		self.__columnCount+=1


	def getRow(self, index):
		return Matrix(self.__matrix[index])

	def getCollumn(self,index):
		return Matrix(list(map(lambda x: [x[index]], self.__matrix)))

	def transpose(self):
		return Matrix(list(map(list,zip(*self.__matrix))))

	def getRowCount(self):
		return self.__rowCount

	def getCollumnCount(self):
		return self.__columnCount

	def __getDiagonalEqualsMatrix(self):
		matrixDiagonal=self.__matrix.copy()
		assert(self.__columnCount == self.__rowCount), "Dimension Error"

		for i in range(self.__columnCount):
			for j in range(self.__rowCount):
				temprow=[]
				if i !=j  and matrixDiagonal[i][i]!=0 and matrixDiagonal[j][i]!=0:
					temprow= list(map(lambda x: x/matrixDiagonal[i][i]*(-1)*matrixDiagonal[j][i],matrixDiagonal[i]))
					matrixDiagonal[j]=list(map(lambda x, y: x+y, temprow, matrixDiagonal[j]))
		return matrixDiagonal;

	def getDeterminant(self):
		matrixDiagonal=self.__getDiagonalEqualsMatrix()	
		determinant=1.0
		for i in range(self.__rowCount): determinant*=matrixDiagonal[i][i]
		return round(determinant,5)

	def getRang(self):
		matrixDiagonal=self.__getDiagonalEqualsMatrix()	
		rang = 0
		for i in range(self.__rowCount):
			countZero=0
			for j in range(self.__columnCount): 
				if matrixDiagonal[i][j]==0: countZero+=1
			if countZero != self.__columnCount: rang+=1
		return rang

	# def trigon(self,n):
	# 	det=1
	# 	new_list = list(self.__matrix)
	# 	for k in range(0, n-1):
	# 		max_s=k
	# 		for i in range(k+1, n):
	# 			if (abs(new_list[i][k])>abs(new_list[k][k])):
	# 				max_s=i
	# 			else:
	# 				break
	# 		if(max_s != k):
	# 			det= det*(-1)
	# 			for j in range(0,n):
	# 				temp=new_list[k][j]
	# 				new_list[k][j]=new_list[max_s][j]
	# 				new_list[max_s][j]=temp
	# 		if(new_list[k][k]!=0):
	# 			for i in range(k+1, n):
	# 				coeff=(new_list[i][k]*1.0)/new_list[k][k]
	# 				for j in range(0, n):
	# 					new_list[i][j]=new_list[i][j]-coeff*new_list[k][j]
	# 					new_list[i][j]=round(new_list[i][j],5)
	# 					if abs(new_list[i][j])<=0.00001:
	# 						new_list[i][j]=0
	# 		else:
	# 			break
	# 	return new_list

	# def getDeterminant(self,n):
	# 	det=1
	# 	new_matrix = list(self.__matrix)
	# 	new_matrix = new_matrix.trigon(n)
	# 	for i in range(0, n):
	# 	    det= det * new_matrix[i][i]
	# 	return(det)
