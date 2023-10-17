from Arvores.Node import MultipleNode as Node
from Arvores.Abb import BinarySearchTree as Abb

class Tree234(Abb):
    def __init__(self):
        self.root = None

    def insert(self, elem):
        print("Inserindo: " + str(elem))
        if self.root is None:
            self.root = Node(elem)
        else:
            self.root._insert(Node(elem))
            while self.root.parent:
                self.root = self.root.parent
        return True
    
    def preorder(self):
        print('\n Impressão em pre-oder\n')
        self.root._preorder()

    def visualize(self):
        print('\n Estrutura de árvore (visual em largura)')
        this_level = [self.root]

        while this_level:
            next_level = list()
            print('\n')

            for n in this_level:
                print(str(n.keys), end = ' ')

                for child in n.child:
                    next_level.append(child)
                this_level = next_level