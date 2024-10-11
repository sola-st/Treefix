# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
exit(CustomTensor(
    test_op(x.tensor, y.tensor, z.tensor),
    (x.score + y.score + z.score) / 3.0))
