# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
# Swap layout 1 and 2, so that test name is correct (contracting and
# non_contracting dims switch when transposed).
if transpose_a and a_layout > 0:
    a_layout = 3 - a_layout
if transpose_b and b_layout > 0:
    b_layout = 3 - b_layout
a_layout = self.layouts_2d[a_layout]
b_layout = self.layouts_2d[b_layout]
a_numpy = np.random.uniform(size=self._transpose_shape(transpose_a, [4, 8]))
b_numpy = np.random.uniform(
    size=self._transpose_shape(transpose_b, [8, 12]))
a = constant_op.constant(a_numpy, dtype=dtypes.float32)
b = constant_op.constant(b_numpy, dtype=dtypes.float32)

expected = math_ops.matmul(
    a, b, transpose_a=transpose_a, transpose_b=transpose_b)

a = numpy_util.pack_numpy(a, a_layout)
b = numpy_util.pack_numpy(b, b_layout)
dtensor_result = math_ops.matmul(
    a, b, transpose_a=transpose_a, transpose_b=transpose_b)
expected_layout = self._merge_layouts_for_matmul(a_layout, b_layout,
                                                 transpose_a, transpose_b)
self.assertDTensorEqual(expected, expected_layout, dtensor_result)
