# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = array_ops.zeros([1, 2])
with backprop.GradientTape() as tape:
    tape.watch(x)
    r = pfor_control_flow_ops.vectorized_map(
        lambda t: array_ops.gather(x, t, axis=-1), math_ops.range(2))
self.assertAllClose([[1., 1.]], tape.gradient(r, x))
