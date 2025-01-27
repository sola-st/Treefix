# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/lu_op_test.py
lower_np, upper_np, perm_np, verification_np = self.evaluate(
    [lower, upper, perm, verification])

self.assertAllClose(x, verification_np)
self.assertShapeEqual(x, lower)
self.assertShapeEqual(x, upper)

self.assertAllEqual(x.shape[:-1], perm.shape.as_list())

# Check dtypes are as expected.
self.assertEqual(x.dtype, lower_np.dtype)
self.assertEqual(x.dtype, upper_np.dtype)
self.assertEqual(output_idx_type.as_numpy_dtype, perm_np.dtype)

# Check that the permutation is valid.
if perm_np.shape[-1] > 0:
    perm_reshaped = np.reshape(perm_np, (-1, perm_np.shape[-1]))
    for perm_vector in perm_reshaped:
        self.assertAllClose(np.arange(len(perm_vector)), np.sort(perm_vector))
