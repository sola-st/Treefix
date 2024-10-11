# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
    a = math_ops.range(3, dtype=dtypes.float32)
    tape.watch(a)
    index = constant_op.constant(1, dtype=dtypes.int64)
    b = 2. * a[index]
grad = tape.gradient(b, a)
self.assertAllEqual(self.evaluate(grad), [0., 2., 0.])
