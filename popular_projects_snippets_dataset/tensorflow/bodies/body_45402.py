# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements_test.py
v = []
u = []
w = []
while x > 0:
    x -= 1
    if x % 2 == 0:
        if x % 3 != 0:
            u.append(x)
        else:
            w.append(x)
            continue
    v.append(x)
exit((v, u, w))
