# FLAG: pbctf{flag+here}
FLAG = b"pb" # B -> BYTES

# Library 

import random
import binascii
# TEST bytes_to_bits

def bytes_to_bits(inp):
    res = []
    for v in inp:
        res.extend(list(map(int, format(v, '08b'))))
    return res
def bits_to_bytes(inp):
    res = []
    for i in range(0, len(inp), 8):
        res.append(int(''.join(map(str, inp[i:i+8])), 2))
    return bytes(res)

flag = bytes_to_bits(FLAG)
flag_decode = bits_to_bytes(flag)
print(ord('p'))
print(ord('b'))
print(flag)
print(flag_decode)

########## Understood bytes_to_bits and bits_to_bytes ##########

# TEST keygen(ln)

def keygen(ln):
    # Generate a linearly independent key
    arr = [ 1 << i for i in range(ln) ]

    for i in range(ln):
        for j in range(i):
            if random.getrandbits(1):
                arr[j] ^= arr[i]
    for i in range(ln):
        for j in range(i):
            if random.getrandbits(1):
                arr[ln - 1 - j] ^= arr[ln - 1 - i]

    return arr

## TEST random.getrandbits(1)

# a = random.getrandbits(k) # La random 1 so tu 0 den 1<<k , voi k la so bit
# print("a: ",a)
u = keygen(4)
print("keygen: ",u)


########## temperature skip keygen ##########

# TEST gen_keystream

def gen_keystream(key):
    ln = len(key)
    
    # Generate some fake values based on the given key...
    fake = [0] * ln
    for i in range(ln):
        for j in range(ln // 3):
            if i + j + 1 >= ln:
                break
            fake[i] ^= key[i + j + 1]

    # Generate the keystream
    res = []
    for i in range(ln):
        t = random.getrandbits(1)
        if t:
            res.append((t, [fake[i], key[i]]))
        else:
            res.append((t, [key[i], fake[i]]))

    # Shuffle!
    random.shuffle(res)

    keystream = [v[0] for v in res]
    public = [v[1] for v in res]
    return keystream, public

########## Understood keystream ##########

# TEST hex()

uu = FLAG.hex()
print("uu: ",uu)

binary_string = binascii.unhexlify(uu)
print("binary string: ",binary_string)

########## Understood hex ##########

# TEST arr 

arr = [0]*5
arr[1]=2
arr[3]=4
print(arr)

# TEST for down: for i in range(5,0,-1)

for i in range(5,-1,-1):
    print(i)

# TEST gen

u = random.getrandbits(1)
print(u)
if(u):
    print("Y")
else:
    print("N")

# TEST list(range(i+1,ln))

arr = list(range(1,5)) # Tao hoan vi
random.shuffle(arr)
print("arr: ",arr)
for j in arr[:2]:
    print("j: ",j)