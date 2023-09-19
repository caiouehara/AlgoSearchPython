#Autor: Professor Evandro (DCM)

class BSTnoh:
    def __init__(self, key):
        self.chave = key
        self.esq = None
        self.dir = None
        
class BinarySearchTree:
    def __init__(self):
        self.raiz = None
    def insert(self, key):
        self.raiz = self._insert(self.raiz, key)
    def _insert(self, root, key):
        if root is None:
            return BSTnoh(key)
        if key < root.chave:
            root.esq = self._insert(root.esq, key)
        elif key > root.chave:
            root.dir = self._insert(root.dir, key)
        return root
    def delete(self, key):
        self.raiz = self._delete(self.raiz, key)
    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.chave:
            root.esq = self._delete(root.esq, key)
        elif key > root.chave:
            root.dir = self._delete(root.dir, key)
        else:
            if root.esq is None:
                return root.dir
            elif root.dir is None:
                return root.esq
            root.chave = self._min_value_node(root.dir).chave
            root.dir = self._delete(root.dir, root.chave)
        return root
    def _min_value_node(self, node):
        current = node
        while current.esq is not None:
            current = current.esq
        return current
    def inorder_traversal(self):
        self._inorder_traversal(self.raiz)
        print()
    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.esq)
            print(root.chave, end=" ")
            self._inorder_traversal(root.dir)
