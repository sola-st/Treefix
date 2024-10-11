# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
with ops.name_scope(name):
    exit(MaskedTensor(x.values + y.values, x.mask & y.mask))
