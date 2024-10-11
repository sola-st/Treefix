# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
p = array_ops.placeholder(dtypes.bool, name='p_hold')
x = array_ops.placeholder(dtypes.int32, name='x_hold')
y = array_ops.placeholder(dtypes.int32, name='y_hold')
z = control_flow_ops.cond(p, lambda: x, lambda: y)
array_ops.identity(z, name='result')
