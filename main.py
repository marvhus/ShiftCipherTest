from random import randrange

BASE = 32
RANGE = 94


def cipher(text):
    key = lambda : ((randrange(256) - BASE) % RANGE) + BASE
    func = lambda c, k : (((c - BASE) + k) % RANGE) + BASE
    
    xs = ''
    ks = ''
    for c in text:
        k = key()
        xs += chr(func(ord(c), k))
        ks += chr(k)
    return xs, ks

def plain(text, key):
    func  = lambda c, k : (((c - BASE) - k) % RANGE) + BASE
    
    xs = ''
    for c, k in zip(text, key):
        xs += chr(func(ord(c), ord(k)))
    return xs
    

text = 'hello world'

xs, ks = cipher(text)
normal = plain(xs, ks)

print('before =', text)
print('cipher =', xs)
print('plain  =', normal)
print('key    =', ks)
