class StackList:
 
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python
    def is_empty(self):
    # Tulis kode di sini
        return len(self.items) == 0
    
    def push(self, url):
    # Tulis kode di sini (Petunjuk: gunakan append)
        self.items.append(url)

    def pop(self):
    # Tulis kode di sini (Petunjuk: pastikan tidak kosong, lalu gunakan pop)
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop
    
    def peek(self):  
 # Tulis kode di sini (Petunjuk: kembalikan elemen indeks terakhir [-1])
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]       
    def size(self):
        return len(self.items)
        
    # Tulis kode di sini (Petunjuk: gunakan len())

myHistory = StackList()

myHistory.push('chatgpt.com')
myHistory.push('idlix')
myHistory.push('cara menjadi sekeren dapa')

print("History: ", myHistory.items)
print("Pop: ", myHistory.pop())
print("History after Pop: ", myHistory.items)
print("Peek: ", myHistory.peek())
print("isEmpty: ", myHistory.is_empty())
print("Size: ", myHistory.size())
