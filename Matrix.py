import copy
class Matrix():
	def __init__(self, lists):
		assert(lists), "This is empty list from initialization matrix"
		self.__matrix=copy.deepcopy(lists)
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
		for i in range(len(self.__matrix)):
			for j in range(len(self.__matrix[0])):
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
		return Matrix(list(map(lambda x: list(map(lambda y: y*other ,x)), self.__matrix)).copy())

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

	def getInverseMatrix(self):
		assert(self.__rowCount==self.__columnCount), "Error Dimension!"
		temp=Matrix(copy.deepcopy(self.__matrix))
		initEiMatrix=[]
		for i in range (self.__rowCount):
			row=[0]*self.__rowCount
			initEiMatrix.append(row)
		for i in range(self.__rowCount): 
			initEiMatrix[i][i]=1
		temp.__addExtendetMatrix(Matrix(initEiMatrix))
		matrixDiagonalList=temp.getDiagonalEqualsMatrix().getMatrixInList()
		invertMatrix=[]
		for i in range(self.__rowCount):
			assert( matrixDiagonalList[i][i]!=0),"Determinant Matrix is zero"
			rows=list(map(lambda x: x/matrixDiagonalList[i][i],matrixDiagonalList[i]))
			invertMatrix.append(rows[self.__rowCount:])

		return Matrix(invertMatrix)


	def __pow__(self, N):
		temp=self
		for i in range(N-1): temp=temp*self
		return temp


	def getMatrixInList(self):
		newmatrix=copy.deepcopy(self.__matrix)
		return newmatrix

	def addRow(self, matrixRow):
		self.__matrix.append(matrixRow.__matrix[0])
		self.__rowCount+=1

	def __addExtendetMatrix(self, matrixEx):
		assert(self.__rowCount == matrixEx.getRowCount()),"Error Dimension!"
		list(map(lambda x, y: list(map(lambda z:x.append(z),y)),self.__matrix, matrixEx.__matrix))
		self.__columnCount+=matrixEx.__columnCount

	def addColumn(self,matrixCollumn):
		assert(self.__rowCount == matrixCollumn.__rowCount), "Error Dimension!"
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

	def getDiagonalEqualsMatrix(self):
		matrixDiagonal=copy.deepcopy(self.__matrix)
		assert((self.__columnCount == self.__rowCount) or(2*self.__rowCount == self.__columnCount)), "Dimension Error"

		for i in range(self.__rowCount):
			for j in range(self.__rowCount):
				temprow=[]
				if i !=j  and matrixDiagonal[i][i]!=0 and matrixDiagonal[j][i]!=0:
					temprow= list(map(lambda x: x/matrixDiagonal[i][i]*(-1)*matrixDiagonal[j][i],matrixDiagonal[i]))
					matrixDiagonal[j]=list(map(lambda x, y: x+y, temprow, matrixDiagonal[j]))
		return Matrix(matrixDiagonal)

		

	def getDeterminant(self):
		matrixDiagonal=copy.deepcopy(self.getDiagonalEqualsMatrix().__matrix)	
		determinant=1.0
		for i in range(self.__rowCount): determinant*=matrixDiagonal[i][i]
		return round(determinant,5)

	def getRang(self):
		matrixDiagonal=copy.deepcopy(self.getDiagonalEqualsMatrix().__matrix.copy())
		rang = 0
		for i in range(self.__rowCount):
			countZero=0
			for j in range(self.__columnCount): 
				if matrixDiagonal[i][j]==0: countZero+=1
			if countZero != self.__columnCount: rang+=1
		return rang