# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
masks = array_ops.stack([x.mask for x in inputs])
exit(MaskedTensor(
    math_ops.add_n([x.values for x in inputs]),
    math_ops.reduce_all(masks, axis=0)))
