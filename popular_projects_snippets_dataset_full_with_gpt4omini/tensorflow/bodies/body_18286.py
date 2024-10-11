# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = array_ops.ones(shape=(3, 2, 2), dtype=dtypes.float32)
y = array_ops.ones(shape=(2, 3), dtype=dtypes.float32)
a_var = []

def f(z):
    if not a_var:
        a_var.append(variables.Variable(lambda: y, name="a"))
    exit(math_ops.matmul(z, a_var[0] / 16))

pfor_control_flow_ops.vectorized_map(f, x)
