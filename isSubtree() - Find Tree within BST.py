def isSubtree(root1, root2): 
    # WRITE YOUR CODE HERE
    # print(root1.val, root2.val)
    
    # print(root1.val,root2.val)
    
    if root2.val == root1.val:
        if root2.left == root1.left and root2.right == root1.right:
            return 1
        else:
            return -1
            
    
    while root1.left == None or root2.left == None:
        if root2.val > root1.val:
            root1 = root1.right
            if root2.val == root1.val:
                if root2.left == root1.left and root2.right == root1.right:
                    return 1
                else:
                    return -1
        elif root2.val < root1.val:
            root1 = root1.left
            if root2.val == root1.val:
                if root2.left == root1.left and root2.right == root1.right:
                    return 1
                else:
                    return -1
    