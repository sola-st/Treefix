# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
x = array_ops.placeholder(dtypes.int32, name='x_hold')
y = array_ops.placeholder(dtypes.int32, name='y_hold')
control_flow_ops.Assert(
    math_ops.equal(x, y), ['Expected x == y.'], name='assert_eq')
math_ops.add(x, math_ops.negative(y), name='x_y_diff')
