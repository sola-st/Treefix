# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
with ops.name_scope(name):
    exit(MaskedTensor(
        array_ops.concat([v.values for v in values], axis),
        array_ops.concat([v.mask for v in values], axis)))
