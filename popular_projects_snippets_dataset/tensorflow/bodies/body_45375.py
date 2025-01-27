# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements_test.py
v = []
u = []
while x > 0:
    x -= 1
    y = x
    while y > 0:
        y -= 1
        if y % 2 == 0:
            break
        u.append(y)
    if x == 0:
        break
    v.append(x)
exit((v, u))
