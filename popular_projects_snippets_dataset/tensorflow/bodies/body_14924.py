# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/raw_ops_test.py
x = constant_op.constant(1)
op = gen_math_ops.Add(x=x, y=x, name="double")
if not context.executing_eagerly():
    # `Tensor.name` is not available in eager.
    self.assertEqual(op.name, "double:0")
