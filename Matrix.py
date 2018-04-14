class Matrix():
	def __init__(self, lists):
		assert(lists), "This is empty list from initialization matrix"
		self.__matrix=lists
		self.__rowCount=len(self.__matrix)
		self.__columnCount= len(self.__matrix[0])
		for i in range(len(self.__matrix)):
			assert (len(self.__matrix[i]) == self.__columnCount), "Not rectangular matrix"


	def __add__(self,other):
		return Matrix(list(map(lambda a,b: map( lambda c,d : c+d ,a,b), self.__matrix, other.__matrix)))

	def __str__(self):
		return str(self.getMatrixInList())

	def __mul__(self,other):
		assert isinstance(other,(int,float)) or isinstance(other, Matrix), "This is not matrixs or , Matrix and Scalar"
		if isinstance(other, Matrix) :
			return self.__matrixMul(other)
		elif isinstance(other,(int,float)):
			return self.__scalarMul(other)


	def __scalarMul(self,other):
		return Matrix(list(map(lambda x: map(lambda y: y*other ,x), self.__matrix)))

	def __matrixMul(self,other):
		__mat=[]
		assert self.__rowCount==other.__columnCount, "Dimension Error!"
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

	def addRow(self, row):
		self.__matrix.append(row)

	def addColumn(self,collumn):
		list(map(lambda x, y: x.append(y[0]),self.__matrix, collumn.__matrix))


	def getRow(self, index):
		return Matrix(self.__matrix[index])

	def getCollumn(self,index):
		return Matrix(map(lambda x: [x[index]], self.__matrix))

	def transpose(self):
		return Matrix(list(map(list,zip(*self.__matrix))))
