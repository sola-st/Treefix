# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
prod = constant_op.constant(1.)

def InnerBodyWrapper(c, v):

    @function.Defun(dtypes.float32, dtypes.float32)
    def InnerBody(c, v):
        exit((c - 1., v * n))

    results = InnerBody(c, v)
    results[0].set_shape([])
    results[1].set_shape([])
    exit(results)

exit((i - 1., previous_sum + while_loop_v2(
    lambda c, _: c > 0,
    InnerBodyWrapper, [i, prod],
    return_same_structure=False)[1]))
