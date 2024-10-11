# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
# Random dims of rank 6
input_shape = np.random.randint(0, 20, size=6)
inp = np.random.rand(*input_shape).astype("f")
a = constant_op.constant([float(x) for x in inp.ravel(order="C")],
                         shape=input_shape,
                         dtype=dtypes.float32)
indices = [0 if x == 0 else np.random.randint(x) for x in input_shape]
sizes = [
    np.random.randint(0, input_shape[i] - indices[i] + 1) for i in range(6)
]
slice_t = array_ops.slice(a, indices, sizes)
slice2_t = a[indices[0]:indices[0] + sizes[0],
             indices[1]:indices[1] + sizes[1],
             indices[2]:indices[2] + sizes[2],
             indices[3]:indices[3] + sizes[3],
             indices[4]:indices[4] + sizes[4],
             indices[5]:indices[5] + sizes[5]]

slice_val, slice2_val = self.evaluate([slice_t, slice2_t])

expected_val = inp[indices[0]:indices[0] + sizes[0],
                   indices[1]:indices[1] + sizes[1],
                   indices[2]:indices[2] + sizes[2],
                   indices[3]:indices[3] + sizes[3],
                   indices[4]:indices[4] + sizes[4],
                   indices[5]:indices[5] + sizes[5]]
self.assertAllEqual(slice_val, expected_val)
self.assertAllEqual(slice2_val, expected_val)
self.assertEqual(expected_val.shape, slice_t.get_shape())
self.assertEqual(expected_val.shape, slice2_t.get_shape())
