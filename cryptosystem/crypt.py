import sys
import random

c = 0
r = 0
argc = len(sys.argv)

with open(sys.argv[1], 'r') as infile, open(sys.argv[2], 'w') as outfile:
    if argc < 3 or argc > 4 or infile is None or outfile is None:
        print("使用法: crypt infile outfile [key]", file=sys.stderr)
    if argc == 4:
        random.seed(ord(sys.argv[3]))
    chars = list(infile.read())
    writes = ''
    while len(chars) > 0:
        c = chars.pop(0)
        r = 0
        r = random.randint(0, 255)
        writes = writes + chr(ord(c) ^ r)
    outfile.write(writes)
