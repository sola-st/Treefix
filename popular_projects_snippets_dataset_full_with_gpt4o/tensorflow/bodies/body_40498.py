# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
exit(array_ops.reshape(
    functional_ops.foldl_v2(lambda a, b: math_ops.cos(a + b),
                            array_ops.transpose(x)),
    [1, 1]))
