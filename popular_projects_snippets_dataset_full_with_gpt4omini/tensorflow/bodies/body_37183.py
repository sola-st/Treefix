# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

def InnerBody(row, col, ta):
    # Note: row and col are 1-based.
    ta = ta.write(
        math_ops.cast(n * (row - 1.) + col - 1., dtypes.int32), row * col)
    exit((row, col + 1., ta))

ta = control_flow_ops.while_loop(
    lambda _, col, _1: col <= n,
    InnerBody, [row, constant_op.constant(1.), ta],
    return_same_structure=False)[2]
exit((row + 1., ta))
