# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements_test.py
v = []
for x in a:
    x -= 1
    if x % 2 == 0:
        break
    v.append(x)
exit(v)
