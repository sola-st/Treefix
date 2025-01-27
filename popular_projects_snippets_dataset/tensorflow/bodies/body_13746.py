# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
exit(math_ops.reduce_all(
    math_ops.equal(
        array_ops.concat(
            [array_ops.shape(a), array_ops.shape(b)], 0),
        array_ops.concat(
            [array_ops.shape(b), array_ops.shape(a)], 0))))
