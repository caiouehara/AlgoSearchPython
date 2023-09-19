#Autor: Professor Evandro (DCM)

class BSTnoh:
    def __init__(self, key):
        self.key = key
        self.esq = None
        self.dir = None

    def getEsq(self):
        if self.esq != None:
            return self.esq

    def getDir(self):
        if self.dir != None:
            return self.dir

    def getKey(self):
        return self.key
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.items = []

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return BSTnoh(key)
        if key < root.key:
            root.esq = self._insert(root.esq, key)
        elif key > root.key:
            root.dir = self._insert(root.dir, key)
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):

        if root is None:
            return root
        if key < root.key:
            root.esq = self._delete(root.esq, key)
        elif key > root.key:
            root.dir = self._delete(root.dir, key)
        else:
            if root.esq is None:
                return root.dir
            elif root.dir is None:
                return root.esq
            root.key = self._min_value_node(root.dir).key
            root.dir = self._delete(root.dir, root.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.esq is not None:
            current = current.esq
        return current

    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.esq)
            print(root.key, end=" ")
            self._inorder_traversal(root.dir)
    

    def inorder(self):
        """ Retorna lista de nos em ordem """
        self.items = []
        self.__inorder(self.root)
        return self.items

    def __inorder(self, n):
        if(n == None):
            return
        else:
            self.__inorder(n.getEsq())
            self.items.append(n.getKey())
            self.__inorder(n.getDir())

    def preorder(self):
        self.items = []
        self.__preorder(self.root)
        return self.items

    def __preorder(self, n):
        if(n == None):
            return
        else:
            self.items.append(n.getKey())
            self.__preorder(n.getEsq())
            self.__preorder(n.getDir())

    def postorder(self):
        self.items = []
        self.__postorder(self.root)
        return self.items

    def __postorder(self, n):
        if(n == None):
            return
        else:
            self.__postorder(n.getEsq())
            self.__postorder(n.getDir())
            self.items.append(n.getKey())
