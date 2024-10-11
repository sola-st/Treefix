# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
# This tests multiple outputs.
x = array_ops.placeholder(dtypes.float32, name='x_hold')
y = array_ops.placeholder(dtypes.float32, name='y_hold')
math_ops.matmul(x, y, name='x_y_prod')
math_ops.add(x, y, name='x_y_sum')
