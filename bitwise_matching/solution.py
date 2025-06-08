

def next_number_with_same_bits(n):

    if n <= 0:
        return -1
    
    num_bits = bin(n).count('1')
    
    next_num = n + 1
    
    while True:
        if bin(next_num).count('1') == num_bits:
            return next_num
        next_num += 1
        
        if next_num > (1 << 64):
            return -1

def next_number_with_same_bits_bitwise(n):
    
    if n <= 0:
        return -1
    
    c = n
    c0 = 0  
    c1 = 0  
    
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1
    
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1
    
    p = c0 + c1
    
    n |= (1 << p)
    
    n &= ~((1 << p) - 1)
    
    n |= (1 << (c1 - 1)) - 1
    
    return n