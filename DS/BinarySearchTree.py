"""Imagine an inverted real tree, that's a tree in Computer Science.
Fundamental building block of a tree is called a Node and the Node where
a tree starts is called the 'Root'. The Root Node can branch out to have
multiple child Nodes and so on, that's how a tree data structure is formed.
The Nodes with no child Nodes (meaning the node/s at which the tree ends) are
called Leaf/Leaves of the Tree, as you would've imagined and the branches
connecting the Nodes are called edges of a Tree. Binary Tree is a kind
of a tree with atmost 2 child Nodes at every level of the tree, also Binary
Search Tree is a kind of a Binary Tree in which the value of left child Node
is less than the parent Node and the value of right Node is greater than the
parent Node."""


class Node:
  def __init__(self, value):
    self.value = value # value of the node
    self.left = None
    self.right = None
    self.level = None # level of the node

  def __str__(self):
    return str(self.value) # return value as a string

class BST:

  def __init__(self):
    self.root = None

  def create(self, val):
    if self.root == None:
      self.root = Node(val)
    else:
      current = self.root
      while True:
        if val < current.value:
          if current.left:
            current = current.left # if left node exists, assign current node as left node
          else:
            current.left = Node(val) # else assign Node as left leaf.
            break
        elif val > current.value:
          if current.right:
            current = current.right
          else:
            current.right = Node(val)
            break
        else:
          break

  def bft(self): #Breadth-First/Level-order Traversal

    self.root.level = 0
    queue = [self.root]
    out = []
    current_level = self.root.level

    while len(queue) > 0:

       current_node = queue.pop(0)

       if current_node.level > current_level:
          current_level += 1
          out.append("\n")

       out.append(str(current_node.value) + " ")

       if current_node.left:

          current_node.left.level = current_level + 1
          queue.append(current_node.left)


       if current_node.right:

          current_node.right.level = current_level + 1
          queue.append(current_node.right)


    print "".join(out)

  def dft(self):  # Depth-first Traversal

    self.root.level = 0
    stack_arr = [self.root]
    out = []
    current_level = self.root.level
    while len(stack_arr) > 0:

      current_node = stack_arr.pop()

      if current_node.level > 0:
        current_level += 1
        out.append("\n")

      out.append(str(current_node.value) + " ")

      if current_node.left:
        current_node.left.level = current_level + 1
        stack_arr.append(current_node.left)

      if current_node.right:
        current_node.right.level = current_level + 1
        stack_arr.append(current_node.right)

    print "".join(out)

  def preorder(self, node):
    if node is not None:
      print node.value
      self.preorder(node.left)
      self.preorder(node.right)

  def postorder(self, node):
    if node is not None:
      self.postorder(node.left)
      self.postorder(node.right)
      print node.value

  def inorder(self, node):
    if node is not None:
      self.inorder(node.left)
      print(node.value)
      self.inorder(node.right)

  def height(self, node): # height of the tree is the number of edges a tree has till its leaf.
    if node is None:
      return -1
    else:
      return max(1 + self.height(node.left), 1 + self.height(node.left))

tree = BST()
arr = [8,3,1,6,4,7,10,14,13]
for i in arr:
    tree.create(i)
print 'Breadth-First Traversal'
tree.bft()
print 'Depth-First Traversal'
tree.dft()
print 'pre-order Traversal'
tree.preorder(tree.root)
print 'post-order Traversal'
tree.postorder(tree.root)
print 'in-order Traversal'
tree.inorder(tree.root)
print 'height of the tree'
print tree.height(tree.root)
