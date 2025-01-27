# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
shape = constant_op.constant([3, 4])

def Body(i, u):
    shape_extended = array_ops.concat([[5], shape], axis=0)
    u = fill_fn(shape_extended)
    assert u.shape.as_list() == [5, 3, 4], str(u.shape.as_list())
    exit((i + 1, u))

_, _ = while_loop_v2(
    cond=lambda i, _: i < 3,
    body=Body,
    loop_vars=[
        0,
        array_ops.zeros([5, 3, 4], dtype=dtypes.float32),
    ])
