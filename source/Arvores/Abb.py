from Arvores.Tree import Tree
from Arvores.Node import SimpleNode as Node

class BSTnoh(Node):
    def __init__(self, key):
        super().__init__(key)

class BinarySearchTree(Tree):
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return BSTnoh(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):

        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._min_value_node(root.right).key
            root.right = self._delete(root.right, root.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.left)
            print(root.key, end=" ")
            self._inorder_traversal(root.right)
    
    def inorder(self):
        """ Retorna lista de nos em ordem """
        self.items = []
        self.__inorder(self.root)
        return self.items

    def __inorder(self, n):
        if(n == None):
            return
        else:
            self.__inorder(n.getleft())
            self.items.append(n.getKey())
            self.__inorder(n.getright())

    def preorder(self):
        self.items = []
        self.__preorder(self.root)
        return self.items

    def __preorder(self, n):
        if(n == None):
            return
        else:
            self.items.append(n.getKey())
            self.__preorder(n.getleft())
            self.__preorder(n.getright())

    def postorder(self):
        self.items = []
        self.__postorder(self.root)
        return self.items

    def __postorder(self, n):
        if(n == None):
            return
        else:
            self.__postorder(n.getleft())
            self.__postorder(n.getright())
            self.items.append(n.getKey())