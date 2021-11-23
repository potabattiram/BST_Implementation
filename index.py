import pandas as pd

# NODE Creation 
class _Node:
    __slots__ = '_element','_left','_right'

    def __init__(self,element,left,right):
        self._element = element 
        self._left = left
        self._right = right 

# Implementation of BST
class BinarySearchtree:
    def __init__(self):
        self._root = None 

    # Inserts elements into BST
    # If Lesser than Node, inserts it into Left
    # If Greater than Node, inserts it into Right
    def Insert(self,root,e):
        temp = None 
        while root:
            temp = root
            if e == root._element:
                return 
            elif e < root._element:
                root = root._left 
            elif e > root._element:
                root = root._right 

        n = _Node(e,None,None)
        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n 

        else:
            self._root = n
        
    # Inorder always Sorts the elements in ascending order of any BST
    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=' ')
            self.inorder(troot._right)

    # Returns the left-most element, as it is the minimal value 
    def MinSalary(self,root):
        if root._left:
            root = root._left
        print("Minimum Salary: ",root._element)

    # Returns the right-most element, as it is the maximal value
    def MaxSalary(self,root):
        if root._right:
            root = root._right 
        print("Maximum Salary: ", root._element) 


# Reading data using Pandas
data = pd.read_csv('data.csv')
def dataIntegration(data):
    BST = BinarySearchtree()

    # Since we have large number of records, we use FOR loop to insert elements into BST
    for i in range(len(data)):
        BST.Insert(BST._root, data.iloc[i]["Salary"])

    
    BST.MaxSalary(BST._root)
    BST.MinSalary(BST._root)


# Function Call
dataIntegration(data)