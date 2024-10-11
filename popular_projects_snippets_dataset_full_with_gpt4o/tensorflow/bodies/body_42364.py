# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
default = ops.Tensor._USE_EQUALITY

try:
    tf_a = constant_op.constant([1, 1])
    tf_b = constant_op.constant([1, 1])
    tf_c = constant_op.constant([[1, 1], [1, 1]])
    tf_d = constant_op.constant([[1, 2], [1, 2]])
    tf_e = constant_op.constant([1, 1, 1])
    np_a = np.array([1, 1])
    np_b = np.array([1, 1])
    np_c = np.array([[1, 1], [1, 1]])
    np_d = np.array([[1, 2], [1, 2]])
    np_e = np.array([1, 1, 1])

    ops.disable_tensor_equality()
    # We don't do element-wise comparison
    self.assertNotEqual(tf_a, tf_b)
    self.assertNotEqual(tf_a, tf_c)
    self.assertNotEqual(tf_a, tf_d)

    ops.enable_tensor_equality()
    # We do element-wise comparison but can't convert results array to bool
    with self.assertRaises(ValueError):
        bool(tf_a == tf_b)
    self.assertAllEqual(tf_a == tf_b, [True, True])
    with self.assertRaises(ValueError):
        bool(tf_a == tf_c)
    self.assertAllEqual(tf_a == tf_c, [[True, True], [True, True]])
    with self.assertRaises(ValueError):
        bool(tf_a == tf_d)
    self.assertAllEqual(tf_a == tf_d, [[True, False], [True, False]])

    # TODO(b/207402791): re-enable once incompatible shapes supported by XLA.
    if not test_util.is_xla_enabled():
        self.assertFalse(bool(tf_a == tf_e))
        self.assertTrue(bool(tf_a != tf_e))

    self.assertNotAllEqual(tf_a, tf_e)

    with self.assertRaises(ValueError):
        bool(np_a == np_b)
    self.assertAllEqual(np_a == np_b, [True, True])
    with self.assertRaises(ValueError):
        bool(np_a == np_c)
    self.assertAllEqual(np_a == np_c, [[True, True], [True, True]])
    self.assertAllEqual(np_a == np_d, [[True, False], [True, False]])
    self.assertFalse(bool(np_a == np_e))
    self.assertTrue(bool(np_a != np_e))
    self.assertNotAllEqual(np_a, np_e)
finally:
    if default:
        ops.enable_tensor_equality()
    else:
        ops.disable_tensor_equality()
