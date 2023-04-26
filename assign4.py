class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)

        if self.root is None:
            self.root = node
        else:
            current = self.root

            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        break
                    current = current.right

    def find_longest_path(self):
        def _find_longest_path(node):
            if node is None:
                return 0
            
            left_height = _find_longest_path(node.left)
            right_height = _find_longest_path(node.right)

            return max(left_height, right_height) + 1

        return _find_longest_path(self.root)

    def find_minimum(self):
        if self.root is None:
            return None
        
        current = self.root

        while current.left is not None:
            current = current.left

        return current.data

    def swap_left_right(self):
        def _swap_left_right(node):
            if node is None:
                return
            
            node.left, node.right = node.right, node.left
            _swap_left_right(node.left)
            _swap_left_right(node.right)

        _swap_left_right(self.root)

    def search(self, data):
        current = self.root

        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False
    
    def inorder(self, node):
        """
        :type node: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        current = node
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                result.append(node.data)
                current = node.right
        return result
    
if __name__ == '__main__':
    bst = BinarySearchTree()

    # Construct the binary search tree by inserting the values in the order given
    values = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    for value in values:
        bst.insert(value)

    # Print the tree inorder traversal
    print("Inorder traversal of the binary search tree:")
    print(bst.inorder(bst.root))

    # Insert a new node
    bst.insert(5)
    print("Inorder traversal of the binary search tree after inserting 5:")
    print(bst.inorder(bst.root))

    # Find number of nodes in longest path
    print("Number of nodes in longest path:", bst.find_longest_path())

    # Minimum data value found in the tree
    print("Minimum data value in the tree:", bst.find_minimum())

    # Change a tree so that the roles of the left and right pointers are swapped at every node
    bst.swap_left_right()
    print("Inorder traversal of the binary search tree after swapping left and right pointers:")
    print(bst.inorder(bst.root))

    # Search a value
    value = 7
    if bst.search(value):
        print(value, "found in the binary search tree")
    else:
        print(value, "not found in the binary search tree")
