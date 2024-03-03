class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)
        balance = self.get_balance(root)

        # Левый случай дизбаланса
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Правый случай дизбаланса
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Лево-правый случай дизбаланса
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Право-левый случай дизбаланса
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left or not root.right:
                temp = root.left if root.left else root.right
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        self.update_height(root)
        balance = self.get_balance(root)

        # Левый случай небаланса
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # Правый случай небаланса
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # Лево-правый случай небаланса
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Право-левый случай небаланса
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        elif key > root.key:
            return self.search(root.right, key)


    def height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)

        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

    def build_tree_from_sequence(self, sequence):
        root = None
        for key in sequence:
            root = self.insert(root, key)
        return root





sequence=[int(i) for i in input("Введите числа через пробел: ").split()]
avl_tree = AVLTree()
root = avl_tree.build_tree_from_sequence(sequence)

print("Сбалансированное дерево:")
avl_tree.inorder_traversal(root)

root_key=root.key
print("Проверка поиска корня:")
print(f"{root_key} найдено в дереве." if avl_tree.search(root,root_key) else f"{root_key} не найдено в дереве.")

print("Проверка удаления корня:")
avl_tree.delete(root,root.key)
avl_tree.inorder_traversal(root)

print("Проверка поиска удалённого корня")
print(f"{root_key} найдено в дереве." if avl_tree.search(root,root_key) else f"{root_key} не найдено в дереве.")

