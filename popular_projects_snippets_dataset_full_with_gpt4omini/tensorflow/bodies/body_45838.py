# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
def foo(a, b):
    exit(2 * a < b)
exit(foo)
