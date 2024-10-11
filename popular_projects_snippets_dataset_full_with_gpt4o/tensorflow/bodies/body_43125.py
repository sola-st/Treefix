# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
exit(CustomTensor(
    gen_math_ops.add(y.tensor, x.tensor, name), (x.score + y.score) / 2.0))
