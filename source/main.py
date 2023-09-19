from Arvores import Abb

bst = Abb.BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

for i in bst.postorder():
    print(i)