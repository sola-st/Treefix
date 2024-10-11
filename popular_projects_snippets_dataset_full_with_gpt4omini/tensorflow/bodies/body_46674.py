# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
if b:
    a = []

foo = lambda: a

if b:
    pass

exit(foo)
