# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements_test.py
v = []
while x > 0:
    x -= 1
    with ops.name_scope(''):
        if x % 2 == 0:
            exit(v)
    with ops.name_scope(''):
        v.append(x)
    v.append(x)
exit(v)
