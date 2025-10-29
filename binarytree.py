'''class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_rec(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_rec(root.right, key)

    def print_tree(self):
        self._print_tree_rec(self.root, 0)

    def _print_tree_rec(self, node, level):
        if node is not None:
            self._print_tree_rec(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.val))
            self._print_tree_rec(node.left, level + 1)

    def search(self, root, key):
        if root is None or root.val == key:
            return root is not None
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.val, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=' ')

    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.val

    def find_max(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current.val

    def height(self, root):
        if root is None:
            return -1
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            return max(left_height, right_height) + 1

if __name__ == "__main__":
    bt = BinaryTree()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bt.insert(val)

    print("Binary Tree Structure:\n")
    bt.print_tree()

    print("\nSearch for 40:")
    found = bt.search(bt.root, 40)
    print("Found" if found else "Not found")

    print("\nInorder traversal:")
    bt.inorder(bt.root)
    print()

    print("Preorder traversal:")
    bt.preorder(bt.root)
    print()

    print("Postorder traversal:")
    bt.postorder(bt.root)
    print()

    print("\nMinimum value in tree:", bt.find_min(bt.root))
    print("Maximum value in tree:", bt.find_max(bt.root))
    print("Height of tree:", bt.height(bt.root))'''
    
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.value,end="")
            self.inorder(node.right)
            
    def preorder(self,node):
        if node:
            print(node.value,end="")
            self.preorder(node.left)
            self.preorder(node.right)
            
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value,end="")
            
tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)

print("\ninorder trversal")
tree.inorder(tree.root)

print("\npreorder traversal")
tree.preorder(tree.root)

print("\npostorder traversal")
tree.postorder(tree.root)