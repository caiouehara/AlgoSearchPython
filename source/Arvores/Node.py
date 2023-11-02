class SimpleNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def _preorder(self):
        print (self.keys)
        for child in self.child:
            child._preorder()

    def getleft(self):
        if self.left != None:
            return self.left

    def getright(self):
        if self.right != None:
            return self.right

    def getKey(self):
        return self.key
    
class MultipleNode(): 
    def __init__(self, keys, par=None):
        self.keys = list([keys])
        self.parent = par
        self.child = list()

    def __lt__(self, node):
        return self.keys[0] < node.keys[0]

    def _isLeaf(self):
        return len(self.child) == 0

    """
    Função auxiliar para adicionar um novo noh ao original. 
    Controla o split e a dimensão de um noh já existente.
    """

    #Remove, baseado no algoritmo da árvore B do livro do Cormen 
    def _remove(self, elem):
        t = 2
        for i in range(0, len(self.keys)):
            #Caso 1 (Folha)
            if self._isLeaf() and self.keys[i] == elem:
                print('here')
                self.keys.remove(elem)
                break

            for child in self.child:
                print("Trace path: " + str(self.keys) + str(i) + " -> " + str(child.keys))
                
                if self.keys[i] == elem:

                    y = self.child[i]
                    z = self.child[i+1]

                    #Caso 2a
                    if len(y.keys) >= t:
                        self.keys[i] = y.keys[2]
                        y._remove(self.keys[i])

                    #Caso 2b
                    elif len(y.keys) < t:
                        if len(z.keys) >= t:
                            self.keys[i] = z.keys[0]
                            z._remove(self.keys[i]) 

                        #Caso 2c (Fusão)
                        else:
                            y.append(self.keys[i])
                            y.extends(z.keys)

                            self.keys.remove(self.keys[i])
                            del self.child[1]
                else:
                    #Caso 3
                    child._remove(elem)

    def _insertIntoNode(self, new_node):
        for child in new_node.child:
            child.parent = self
        self.keys.extend(new_node.keys)
        self.keys.sort()
        self.child.extend(new_node.child)
        if len(self.child) > 1:
            self.child.sort()
        if len(self.keys) > 3:
            self._split()

    """
    Para inserção de um dado na árvore.
    Procura onde inserir um noh na árvore e o insere recursivamente.
    Esta, é a função interna, usada apenas pelo TAD. 
    """

    def _insert(self, new_node):
        #Caso 1 - Insercao em uma folha
        if self._isLeaf():
            self._insertIntoNode(new_node)
        #Caso 2 - Não é uma folha - Encntra o lugar para inserer e o insere com recursão
        elif new_node.keys[0] > self.keys[-1]:
            self.child[-1]._insert(new_node)
        else:
            # Não gera problema de complexidade? Está varrendo todos os elementos da árvore?
            for i in range(0, len(self.keys)):
                if new_node.keys[0] < self.keys[i]:
                    self.child[i]._insert(new_node)
                    break
    
    #Função "split". É usada quando um noh sofre overflow
    def _split(self):
        left_child = MultipleNode(self.keys[0], self)
        right_child = MultipleNode(self.keys[2], self)
        right_child.keys.append(self.keys[3])

        if self.child:
            self.child[0].parent = left_child
            self.child[1].parent = left_child
            self.child[2].parent = right_child
            self.child[3].parent = right_child
            self.child[4].parent = right_child

            left_child.child = [self.child[0], self.child[1]]
            right_child.child = [self.child[2], self.child[3], self.child[4]]

        self.child = [left_child]
        self.child.append(right_child)
        self.keys = [self.keys[1]]

        #Adiciona o novo noh (resultado do split) ao seu node pai
        if self.parent:
            if self in self.parent.child:
                self.parent.child.remove(self)
            self.parent._insertIntoNode(self)
        else:
            left_child.parent = self
            right_child.parent = self 

    def _preorder(self):
        print (self.keys)
        for child in self.child:
            child._preorder()