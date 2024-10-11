# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
"""A more complex graph, including splits."""
x = array_ops.placeholder(dtypes.float32, shape=[2, 2], name='x')
y = array_ops.placeholder(dtypes.float32, shape=[2, 2], name='y')
for _ in range(3):
    x0, x1 = array_ops.split(x, 2, 0)
    y0, y1 = array_ops.split(y, 2, 0)
    x0 += 1
    y0 += 1
    z = math_ops.matmul(x, y, name='x_y_prod')
    a = array_ops.concat([x0, y1], axis=0, name='concat_x0_y1')
    b = array_ops.concat([y0, x1], axis=0, name='concat_y0_x1')
    x = math_ops.matmul(a, b, name='a_b')
    y = math_ops.add(x, z)
array_ops.identity(y, name='result')
