# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/continue_statements_test.py
v = []
for x in a:
    x -= 1
    if x > 100:
        continue
    try:
        raise ValueError('intentional')
    except ValueError:
        continue
    v.append(x)
exit(v)
