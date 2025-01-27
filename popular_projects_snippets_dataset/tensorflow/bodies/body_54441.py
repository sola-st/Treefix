# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default():
    with self.assertRaises(ValueError):
        math_ops.add([1, 2], [1, 2, 3])
    a = constant_op.constant(1)
    with session.Session() as sess:
        self.evaluate(a)
