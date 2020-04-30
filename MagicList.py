class MagicList :
	def __init__(self):
		self.data = [0]
	
	def findMin(self):
		M = self.data
		''' you need to find and return the smallest
			element in MagicList M.
			Write your code after this comment.
		'''
		if len(M)!=1:
			return min(M[1:])
		else:
			None
	
	def insert(self, E):
		M = self.data
		''' you need to insert E in MagicList M, so that
			properties of the MagicList are satisfied. 
			Return M after inserting E into M.
			Write your code after this comment.
		'''
		
		
		M.append(E)
		i=len(M)-1
		while i >0:
			if M[i]<M[i//2]:
				(M[i],M[i//2])=(M[i//2],M[i])
			i=i-1
		return M
	
	def deleteMin(self):
		M = self.data
		''' you need to delete the minimum element in
			MagicList M, so that properties of the MagicList
			are satisfied. Return M after deleting the 
			minimum element.
			Write your code after this comment.
		'''	
		d=min(M)
		n=len(M)
		for i in range (0,n-1):
			if M[i]==d:
				r=i
				(M[r],M[-1])=(M[-1],M[r])
		M.pop()
		for r in range (0,(n-2)//2):
			if M[2*r]<M[2*r+1] and M[2*r]<M[r]:
				(M[r],M[2*r])=(M[2*r],M[r])
				r=2*r
			elif M[2*r]>M[2*r+1] and M[2*r+1]<M[r]:
				(M[r],M[2*r+1])=(M[2*r+1],M[r])
				r=2*r+1
			elif M[r]<min(M[2*r],M[2*r+1]):
				break
		return M
	
def K_sum(L, K):
	''' you need to find the sum of smallest K elements
		of L using a MagicList. Return the sum.
		Write your code after this comment.
	'''
	M=MagicList()
	for element in L:
		M.insert(element)
	sum=0
	for n in range (K):
		sum=sum+M.findMin()
		M.deleteMin()
		
	return sum
	
if __name__ == "__main__" :
	'''Here are a few test cases'''
	
	'''insert and findMin'''
	M = MagicList()
	M.insert(4)
	M.insert(3)
	M.insert(5)

	x = M.findMin()
	if x == 3 :
		print("testcase 1 : Passed")
	else:
		print("testcase 1 : Failed")
		
	'''deleteMin and findMin'''
	M.deleteMin()
	x = M.findMin()
	if x == 4 :
		print("testcase 2 : Passed")
	else:
		print("testcase 2 : Failed")
		
	'''k-sum'''
	L = [2,5,8,3,6,1,0,9,4]
	K = 4
	x = K_sum(L,K)
	if x == 6 :
		print("testcase 3 : Passed")
	else:
		print("testcase 3 : Failed")

	M2 = MagicList()
	M2.insert(6)
	M2.insert(12)
	M2.insert(9)
	x = M2.findMin()
	if x == 6 :
		print("testcase 4 : Passed")
	else:
		print("testcase 4 : Failed")
		
	'''deleteMin and findMin'''
	M2.deleteMin()
	x = M2.findMin()
	if x == 9 :
		print("testcase 5 : Passed")
	else:
		print("testcase 5 : Failed")
		
	'''k-sum'''
	L = [3,5,2,8,5,7,3,0,5]
	K = 3
	x = K_sum(L,K)
	if x == 5 :
		print("testcase 6 : Passed")
	else:
		print("testcase 6 : Failed")


