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
        # Empty
        if self.is_empty():
            return None

        #Start & #Prev
        root = self.root
        prev = None

        #loop จนเจอ data ที่จะ del
        while root.val != data:
            #วิ่งซ้าย
            if data < root.val:
                prev = root
                root = root.left
            #วิ่งขวา !
            elif data > root.val:
                prev = root
                root = root.right
            #วิ่งไปแล้วไม่เจอ
            if root == None:
                return None
        #กรณีไม่มีลูก
        if root.left == None and root.right == None:
            if prev.left.val == data:
                prev.left = None
            elif prev.right.val == data:
                prev.right = None
        #กรณีมีลูกซ้าย
        elif root.right == None and root.left != None:
            prev.left = root.left
            root = None
        #กรณีมีลูกขวา
        elif root.right != None and root.left == None:
            prev.right = root.right
            root = None
        #กรณีมีลูกขวา-ซ้าย
        elif root.right != None and root.left != None:
            root.val = root.left.val
            root.left = None
        return data
    
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
wow.insert(10)
wow.insert(20)
wow.insert(2)
# wow.inorder(wow.root)
# print()
# wow.preorder(wow.root)
# print()
# wow.postorder(wow.root)
# print()
wow.traverse()
wow.delete(2)
wow.traverse()