from Arvores.Abb import BinarySearchTree
from Arvores.Tree234 import Tree234
import random

def main():
    tree = Tree234()
    #numbers=random.sample(range(100), 25)
    numbers= [35, 10 , 15, 18, 19 ,17, 5, 6, 15,18,20, 30, 50, 40,45, 55, 45, 46, 36, 37 ]

    for x in numbers:
        tree.insert(x)
    tree.visualize()

    tree.remove(15)

    tree.visualize()

main()