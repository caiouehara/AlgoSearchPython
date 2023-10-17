class Tree:
    def __init__(self):
        self.root = None
        self.items = []

    def printTree(self):
        self._printTree(self.root, level=0)

    def _printTree(self, node, level=0):
        if node == None:
            return
        else: 
            self._printTree(node.left, level + 1)
            print(' ' * 4 * level + '-- ' + str(node.key))
            self._printTree(node.right, level + 1)