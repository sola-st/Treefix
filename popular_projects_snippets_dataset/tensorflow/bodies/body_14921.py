# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/raw_ops_test.py
x = constant_op.constant(1)
self.assertEqual([2], self.evaluate(gen_math_ops.Add(x=x, y=x)))
