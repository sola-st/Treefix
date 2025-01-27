# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
with self.cached_session():
    input_shape = [8, 16, 16, 16, 8]
    total_input_size = 1
    for s in input_shape:
        total_input_size *= s
    inputs = [
        i * 1.0 / total_input_size for i in range(1, total_input_size + 1)
    ]
    a = constant_op.constant(inputs, shape=input_shape, dtype=dtypes.float32)

    filter_shape = [1, 1, 1, 8, 8]
    total_filter_size = 1
    for s in filter_shape:
        total_filter_size *= s
    filters = [
        i * 1.0 / total_filter_size for i in range(1, total_filter_size + 1)
    ]
    f = constant_op.constant(
        filters, shape=filter_shape, dtype=dtypes.float32)

    conv_t = nn_ops.conv3d(
        a, filter=f, strides=[1, 1, 1, 1, 1], padding="VALID")
    slice_t = array_ops.slice(conv_t, [0, 1, 1, 1, 0], [1, 1, 1, 1, 8])
    result = self.evaluate(slice_t)
    expected = [
        0.03028321, 0.03132677, 0.03237033, 0.03341389, 0.03445745, 0.035501,
        0.03654456, 0.03758812
    ]
    self.assertAllClose(expected, result.flatten(), rtol=1e-6)
