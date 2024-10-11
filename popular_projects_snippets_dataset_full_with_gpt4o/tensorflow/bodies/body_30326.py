# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_nd_op_test.py
with self.session():
    params = np.ones((3, 3), dtype=np.float32)

    indices_empty = np.empty((0, 2), dtype=np.int32)
    gather_nd_ok_t = array_ops.gather_nd(params, indices_empty)
    gather_nd_ok_val = self.evaluate(gather_nd_ok_t)
    self.assertEqual([0], gather_nd_ok_t.get_shape())
    self.assertAllClose(np.empty((0,), dtype=np.float32), gather_nd_ok_val)

    indices_empty = np.empty((0, 1), dtype=np.int32)
    gather_nd_ok_t = array_ops.gather_nd(params, indices_empty)
    gather_nd_ok_val = self.evaluate(gather_nd_ok_t)
    self.assertEqual([0, 3], gather_nd_ok_t.get_shape())
    self.assertAllClose(np.empty((0, 3), dtype=np.float32), gather_nd_ok_val)

    params_empty = np.empty((0, 3), dtype=np.float32)
    indices_empty = np.empty((0, 2), dtype=np.int32)
    gather_nd_ok_t = array_ops.gather_nd(params_empty, indices_empty)
    gather_nd_ok_val = self.evaluate(gather_nd_ok_t)
    self.assertEqual([0], gather_nd_ok_t.get_shape())
    self.assertAllClose(np.empty((0,), dtype=np.float32), gather_nd_ok_val)

    params_empty = np.empty((0, 3), dtype=np.float32)
    indices_nonempty = np.zeros((1, 2), dtype=np.int32)
    gather_nd_break_t = array_ops.gather_nd(params_empty, indices_nonempty)
    with self.assertRaisesOpError(
        r"Requested more than 0 entries, but params is empty."):
        self.evaluate(gather_nd_break_t)
    self.assertAllClose(np.empty((0,), dtype=np.float32), gather_nd_ok_val)
