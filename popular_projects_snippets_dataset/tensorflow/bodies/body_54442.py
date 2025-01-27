# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    with g._kernel_label_map({"KernelLabelRequired": "overload_1"}):
        with self.assertRaises(ValueError):
            test_ops.kernel_label_required(1)
    a = constant_op.constant(1)
    with session.Session() as sess:
        self.evaluate(a)
