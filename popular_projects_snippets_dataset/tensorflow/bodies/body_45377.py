# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements_test.py
v = []
u = []
while x > 0:
    x -= 1
    y = x
    while y > 1:
        break
    else:
        u.append(y)
        break
    v.append(x)
exit((v, u))
