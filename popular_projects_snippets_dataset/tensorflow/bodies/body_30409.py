# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
with self.cached_session(force_gpu=test.is_gpu_available()):
    a = constant_op.constant([0, 1, 2], dtype=dtypes.int64)

    # Slice using int32 Tensor.
    i = constant_op.constant(1, dtype=dtypes.int32)
    slice_t = a[i]
    slice_val = self.evaluate(slice_t)
    self.assertAllEqual(1, slice_val)
    slice_t = a[i:i + 1]
    slice_val = self.evaluate(slice_t)
    self.assertAllEqual([1], slice_val)

    # Slice using int32 integer.
    i = np.asarray(1).astype(np.int32)
    slice_t = a[i]
    slice_val = self.evaluate(slice_t)
    self.assertAllEqual(1, slice_val)
    slice_t = a[i:i + 1]
    slice_val = self.evaluate(slice_t)
    self.assertAllEqual([1], slice_val)

    slice_t = array_ops.slice(a, [1], [2])
    slice_val = self.evaluate(slice_t)
    self.assertAllEqual([1, 2], slice_val)
