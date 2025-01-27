# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with session.Session():
    var = self.make_variable(shape)
    if axis is None:
        axis_size = 1
        for dim in shape:
            axis_size *= dim
    else:
        axis_size = shape[axis]
    repeats = constant_op.constant(
        np.random.randint(max_repeats, size=[axis_size]), dtype=dtypes.int64)
    repeat_op = array_ops.repeat(var, repeats, axis=axis)
    # Return a scalar to reduce the device-to-host memcopy overhead.
    repeat_op = repeat_op[(0,) * len(shape)]
    self.run_and_time(repeat_op)
