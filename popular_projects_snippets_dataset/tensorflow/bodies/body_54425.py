# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.eager_mode():
    c = constant_op.constant(1.0)
    with ops.Graph().as_default():
        with self.assertRaisesRegex(RuntimeError,
                                    "Attempting to capture an EagerTensor"):
            math_ops.add(c, c)
        c2 = constant_op.constant(2.0)
    with self.assertRaises(TypeError):
        math_ops.add(c2, c2)
