from chunk import Chunk

import pyperclip


f = open("file.txt", "r")
txt = f.read()

ch = Chunk(txt)

print(len(ch))


for i in range(0, len(ch)):
    x = input()
    pyperclip.copy(ch.get_chunk(i))

