# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
def foo():
    exit(a)

if b:
    a = []

exit(foo)
