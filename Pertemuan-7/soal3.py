class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def sisipkan_VIP(head,plat_baru, plat_target):
  if plat_target.next == None:
    plat_target.next = plat_baru
    return head
  plat_baru.next = plat_target.next
  plat_target.next = plat_baru
  return head

plat1 = Node("B 1234 ABC")
plat2 = Node("D 8888 XYZ")
plat3 = Node("A 111 TUV")
plat4 = Node("B 2022 EFG")


plat1.next = plat2
plat2.next = plat3
plat3.next = plat4

plat5 = Node("BM 0404 DL")
plat1 =sisipkan_VIP(plat1, plat5, plat2)
traverseAndPrint(plat1)





  
