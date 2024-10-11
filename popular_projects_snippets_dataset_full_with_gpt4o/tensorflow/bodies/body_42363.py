# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
default = ops.Tensor._USE_EQUALITY

try:
    tf_a = constant_op.constant([1, 2])
    tf_b = constant_op.constant([1, 2])
    tf_c = constant_op.constant([1, 1])
    np_a = np.array([1, 2])
    np_b = np.array([1, 2])
    np_c = np.array([1, 1])

    ops.disable_tensor_equality()
    # We don't do element-wise comparison
    self.assertNotEqual(tf_a, tf_b)
    self.assertNotEqual(tf_a, tf_c)

    # We can compare list of tensors
    self.assertEqual([tf_a, tf_b], [tf_a, tf_b])
    self.assertNotEqual([tf_a, tf_b], [tf_b, tf_b])

    # We can compare existence in a list
    self.assertIn(tf_a, [tf_a, tf_b])
    self.assertIn(tf_a, [tf_b, tf_a])
    self.assertNotIn(tf_a, [tf_b, tf_c])

    ops.enable_tensor_equality()
    # We do element-wise comparison but can't convert results array to bool
    with self.assertRaises(ValueError):
        bool(tf_a == tf_b)
    self.assertAllEqual(tf_a == tf_b, [True, True])
    with self.assertRaises(ValueError):
        bool(tf_a == tf_c)
    self.assertAllEqual(tf_a == tf_c, [True, False])
    self.assertNotAllEqual(tf_a, tf_c)
    with self.assertRaises(ValueError):
        bool(np_a == np_b)
    self.assertAllEqual(np_a == np_b, [True, True])
    with self.assertRaises(ValueError):
        bool(np_a == np_c)
    self.assertAllEqual(np_a == np_c, [True, False])
    self.assertNotAllEqual(np_a, np_c)

    # Warning even though we technically shouldn't be able to compare here,
    # since the id is the same both TF & numpy will handle lists with the same
    # value without raising an error
    self.assertEqual([tf_a, tf_b], [tf_a, tf_b])
    with self.assertRaises(ValueError):
        bool([tf_a, tf_b] == [tf_b, tf_b])
    self.assertEqual([np_a, np_b], [np_a, np_b])
    with self.assertRaises(ValueError):
        bool([np_a, np_b] == [np_b, np_b])

    # Similar to lists we shouldn't be able to do a `in` check such as
    # `if a in [a,b]`. However if `a` is the first element, it works due to
    # short circuiting
    self.assertIn(tf_a, [tf_a, tf_b])
    with self.assertRaises(ValueError):
        bool(tf_a in [tf_b, tf_a])
    with self.assertRaises(ValueError):
        bool(tf_a in [tf_b, tf_c])
    self.assertIn(np_a, [np_a, np_b])
    with self.assertRaises(ValueError):
        bool(np_a in [np_b, np_a])
    with self.assertRaises(ValueError):
        bool(np_a in [np_b, np_c])

    # rank 0
    self.assertAllEqual(
        constant_op.constant(1) == constant_op.constant(1), True)
    self.assertAllEqual(
        constant_op.constant(1) == constant_op.constant(2), False)
    self.assertAllEqual(np.array(1) == np.array(1), True)
    self.assertAllEqual(np.array(1) == np.array(2), False)
finally:
    if default:
        ops.enable_tensor_equality()
    else:
        ops.disable_tensor_equality()
