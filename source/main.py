from Arvores import Abb

bst = Abb.BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder traversal before deletion:")
bst.inorder_traversal()
key_to_delete = 30
bst.delete(key_to_delete)
print("Inorder traversal after deletion:")
bst.inorder_traversal()