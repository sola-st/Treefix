# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
with backprop.GradientTape() as tape:
    inp = constant_op.constant([1.0, 2.0, 3.0], name="in")
    tape.watch(inp)
    out = array_ops.slice(inp, [1], [-1])
grad_actual = self.evaluate(tape.gradient(out, inp))
self.assertAllClose([0., 1., 1.], grad_actual)
