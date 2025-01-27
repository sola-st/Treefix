# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
if constant_op.constant(True):
    exit(a)
else:
    exit(a + a)
