# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
inner1 = array_ops.identity(outer1, name="inner1")
inner2 = array_ops.identity(x2, name="inner2")
inner3 = array_ops.identity(x3, name="inner3")
exit(gradients_impl.gradients([inner1, inner2, inner3, x1],
                                [x1, x2]))
