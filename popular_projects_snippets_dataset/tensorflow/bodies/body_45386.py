# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements_test.py
v = []
while x > 0:
    x -= 1
    if x % 2 == 0:
        continue
    v.append(x)
exit(v)
