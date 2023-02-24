class BSTNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    def is_empty(self):
        if not self.root:
            return True
        return False


    def insert(self, data):
        pNew = BSTNode(data)

        if self.is_empty():
            self.root = pNew
            return
        prev = None
        root = self.root
        while root is not None:
            if root.val > data:
                prev = root
                root = root.left
            elif root.val < data:
                prev = root
                root = root.right
        if prev.val > data:
            prev.left = pNew
        elif prev.val < data:
            prev.right = pNew

    def delete(self, data):
        if self.is_empty():
            return None

        prev = None
        root = self.root

        while root is not None:
            if root.val == data:
                break
            elif root.val > data:
                prev = root
                root = root.left
            else:
                prev = root
                root = root.right

        if root is None:
            return None

        if root.left is None and root.right is None:
            if root == self.root:
                self.root = None
            elif prev.left == root:
                prev.left = None
            else:
                prev.right = None

        elif root.left is None:
            if root == self.root:
                self.root = root.right
            elif prev.left == root:
                prev.left = root.right
            else:
                prev.right = root.right

        elif root.right is None:
            if root == self.root:
                self.root = root.left
            elif prev.left == root:
                prev.left = root.left
            else:
                prev.right = root.left
        
        else:
            parent = root
            kwa = root.left

            #หามากที่สุดของซับซ้าย ของรูทปัจจุบัน(ตัวที่ต้องการลบ)
            while kwa.right is not None:
                parent = kwa
                kwa = kwa.right
            
            #ก้อปค่ามาใส่ตัวปัจจุบัน
            root.val = kwa.val
            
            #
            if parent.left == kwa:
                parent.left = kwa.left
            else:
                parent.right = kwa.left


    def findMin(self):
        root = self.root
        while root.left is not None:
            root = root.left
        return root
    def findMax(self):
        root =self.root
        while root.right is not None:
            root = root.right
        return root

    def preorder(self, root):
        if (root != None):
            print("->", root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self, root):
        if (root != None):
            self.inorder(root.left)
            print("->", root.val, end=" ")
            self.inorder(root.right)
    def postorder(self, root):
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.val, end=" ")
    
    def traverse(self):
        self.preorder(self.root)
        print()
        self.inorder(self.root)
        print()
        self.postorder(self.root)
        print()


wow = BST()
wow.insert(14)
wow.insert(23)
wow.insert(7)
wow.insert(10)
wow.insert(33)
wow.delete(14)
wow.traverse()