# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
with self.cached_session():
    inp = constant_op.constant([1.0, 2.0, 3.0], name="in")
    out = array_ops.slice(inp, [1], [-1])
    grad_actual = self.evaluate(gradients_impl.gradients(out, inp)[0])
self.assertAllClose([0., 1., 1.], grad_actual)
