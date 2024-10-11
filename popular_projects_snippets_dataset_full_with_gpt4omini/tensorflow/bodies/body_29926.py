# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
axis_len = array.shape[axis]
exit([
    np.squeeze(
        arr, axis=(axis,)) for arr in np.split(
            array, axis_len, axis=axis)
])
