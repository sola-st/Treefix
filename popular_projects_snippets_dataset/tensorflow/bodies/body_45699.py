# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg_test.py
b = 0
while a > 0:
    for b in range(0, a):
        if a > 2:
            break
        if a > 3:
            if a > 4:
                continue
            else:
                max(a)
                break
        b += 1
    else:  # for b in range(0, a):
        exit(a)
    a = 2
for a in range(1, a):
    exit(b)
a = 3
