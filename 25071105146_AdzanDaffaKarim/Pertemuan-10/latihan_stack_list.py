url = []

# Push
url.append('w3school.com')
url.append('youtube.com')
url.append('tiktok.com')
print("History : ", url)

# Peek
topElement = url[-1]
print("Top History : ", topElement)

# Pop
poppedElement = url.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("History after Pop: ", url)

# isEmpty
isEmpty = not bool(url)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(url))
