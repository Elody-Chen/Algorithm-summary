# Define a binary tree node
class TreeNode:
    """
    Binary tree node
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTree(nums):
    """
    Transform a list to a binary tree
    :param nums: A tabular representation of a binary tree
    :return: root node of a binary tree
    """
    if len(nums) == 0 or nums == None:
        return None
    n = len(nums)
    root = TreeNode(nums[0])
    deque = list()
    deque.insert(0, root)
    isLeft = True
    for i in range(1, n):
        node = deque[-1]
        if isLeft:
            if nums[i] != None:
                node.left = TreeNode(nums[i])
                deque.insert(0, node.left)
            isLeft = False
        else:
            if nums[i] != None:
                node.right = TreeNode(nums[i])
                deque.insert(0, node.right)
            deque.pop()
            isLeft = True
    return root



# Iteration algorithm to traverse binary tree
class iterativeBinaryTreeTraversal:
    # preorder traversal
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        res = []
        stack = []
        stack.append(root)
        while len(stack):
            currNode = stack.pop()
            res.append(currNode.val)
            if currNode.right:
                stack.append(currNode.right)
            if currNode.left:
                stack.append(currNode.left)
        return res


    # inorder traversal
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        currNode = root
        res = []
        stack = []
        while len(stack) != 0 or currNode is not None:
            while currNode is not None:
                stack.append(currNode)
                currNode = currNode.left
            topNode = stack.pop()
            res.append(topNode.val)
            currNode = topNode.right
        return res


    # postorder traversal
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        res = []
        stack = []
        pre = None
        currNode = root
        while currNode != None or len(stack) != 0:
            while currNode != None:
                stack.append(currNode)
                currNode = currNode.left
            currNode = stack.pop()
            if currNode.right == None or currNode.right == pre:
                res.append(currNode.val)
                pre = currNode
                currNode = None
            else:
                stack.append(currNode)
                currNode = currNode.right
        return res

    # level order traversal
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if root == None:
            return []
        res = []
        queue = []
        queue.append(root)
        while len(queue) != 0:
            curLevelSize = len(queue)
            res.append([])
            for i in range(curLevelSize):
                curNode = queue.pop(0)
                res[-1].append(curNode.val)
                if curNode.left != None:
                    queue.append(curNode.left)
                if curNode.right != None:
                    queue.append(curNode.right)
        return res
    


# Recursive algorithm to traverse binary tree
class recursiveBinaryTreeTraversal:
    # preorder traversal 
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        res = []
        # root -> left -> right
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)

        return res

    # inorder traversal
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        res = []
        # left -> root -> right
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)

        return res

    # postorder traversal
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if root == None:
            return []
        res = []
        # left -> right -> root
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res.append(root.val)
        
        return res



# Rebuild the binary tree from the traversal sequence of the binary tree
class bulidTree:
    def preorderInorder(self, preorder: list, inorder: list) -> TreeNode:
        """
        Rebuild a binary tree based on preorder traversal and inorder traversal of the binary tree.
        :type preorder: list
        :type inorder: list
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        pivotIndex = 0
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                pivotIndex = i
                break
        
        root.left = self.preorderInorder(preorder[1:pivotIndex + 1], inorder[0:pivotIndex])
        root.right = self.preorderInorder(preorder[pivotIndex + 1:], inorder[pivotIndex + 1:])
        return root


    def postorderInorder(self, inorder: list, postorder: list) -> TreeNode:
        """
        Rebuild a binary tree based on postorder traversal and inorder traversal of the binary tree.
        :type inorder: list
        :type postorder: list
        :rtype: TreeNode
        """
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        pivotIndex = 0
        for i in range(len(inorder)):
            if root.val == inorder[i]:
                pivotIndex = i
                break

        root.left = self.postorderInorder(inorder[0:pivotIndex], postorder[0:pivotIndex])
        root.right = self.postorderInorder(inorder[pivotIndex + 1:], postorder[pivotIndex:-1])
        return root
        