# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch_test.py
exit(CustomTensor(
    test_op(a.tensor, b.tensor, c.tensor),
    (a.score + b.score + c.score) / 3.0))
