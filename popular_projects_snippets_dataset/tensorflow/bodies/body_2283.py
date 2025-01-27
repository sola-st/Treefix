# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
with self.assertRaisesIncompatibleShapesError():
    self._testBinary(
        array_ops.broadcast_dynamic_shape,
        np.array([1, 2, 3], dtype=np.int32),
        np.array([4, 5, 6], dtype=np.int32),
        expected=None)
