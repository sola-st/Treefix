# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
def foo(a, b):
    tmp_1001 = 2 * a
    tmp_1002 = tmp_1001 < b
    exit(tmp_1002)
exit(foo)
