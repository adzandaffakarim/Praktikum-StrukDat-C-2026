class Node:
    def __init__(self, url):
        self.url = url
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran

    def is_empty(self):
        # Tulis kode di sini (Petunjuk: periksa apakah top bernilai None)
        return self.count == 0
    
    def push(self, url):
        # Tulis kode di sini
        # 1. Buat Node baru
        # 2. Hubungkan 'next' node baru ke 'top' saat ini
        # 3. Jadikan node baru sebagai 'top' yang baru
        # 4. Tambahkan nilai 'count'
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1
        

    def pop(self):
        # Tulis kode di sini
        # 1. Periksa is_empty()
        # 2. Simpan url dari 'top' saat ini
        # 3. Geser 'top' ke node berikutnya (top = top.next)
        # 4. Kurangi nilai 'count'
        # 5. Kembalikan url yang disimpan
        if self.is_empty():
            return "Stack is empty"
        popnode = self.top
        self.top = self.top.next
        self.count -= 1
        return popnode.url
    
    def peek(self):
        # Tulis kode di sini (Petunjuk: kembalikan nilai url dari 'top')
        if self.is_empty():
            return "Stack is empty"
        return self.top.url
    
    def size(self):
        # Tulis kode di sini
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")
            currentNode = currentNode.next
        print("None")


myHistory = StackLinkedList()
myHistory.push('Instagram.com')
myHistory.push('Youtube.com')
myHistory.push('cara menjadi sekeren dapa')

print("LinkedList: ", end="")
myHistory.traverseAndPrint()
print("Peek: ", myHistory.peek())
print("Pop: ", myHistory.pop())
print("LinkedList after Pop: ", end="")
myHistory.traverseAndPrint()
print("isEmpty: ", myHistory.is_empty())
print("Size: ", myHistory.size())