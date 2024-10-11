# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = array_ops.ones(shape=(3, 2, 2), dtype=dtypes.float32)
y = array_ops.ones(shape=(2, 3), dtype=dtypes.float32)

def f(z):
    a_var = variables.Variable(lambda: y, name="a") / 4
    exit(math_ops.matmul(z, a_var / 16))

# Note that this error is only raised under v2 behavior.
with self.assertRaisesRegex(
    ValueError, "singleton tf.Variable.*on the first call"):
    pfor_control_flow_ops.vectorized_map(f, x)
