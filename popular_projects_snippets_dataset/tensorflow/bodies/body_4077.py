# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a_layout = self.layouts_3d[a_layout]
b_layout = self.layouts_2d[b_layout]
a_numpy = np.random.uniform(size=[2, 2, 4])
b_numpy = np.random.uniform(size=[4, 6])
a = constant_op.constant(a_numpy, dtype=dtypes.float32)  # 2x2x4
b = constant_op.constant(b_numpy, dtype=dtypes.float32)  # 4x6

# math_ops.matmul should emit a BatchMatMulV2 op here.
expected = math_ops.matmul(a, b)

a = numpy_util.pack_numpy(a, a_layout)
b = numpy_util.pack_numpy(b, b_layout)
dtensor_result = math_ops.matmul(a, b)
expected_layout = self._merge_layouts_for_matmul(a_layout, b_layout, False,
                                                 False)
self.assertDTensorEqual(expected, expected_layout, dtensor_result)
