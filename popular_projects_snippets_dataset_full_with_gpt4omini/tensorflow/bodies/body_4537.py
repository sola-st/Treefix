# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_3/multiplex_3_test.py
idx0 = tf.constant([], dtype=tf.int64, shape=[0, 1])
val0 = tf.constant([], dtype=tf.int64)
val5a = tf.constant([1, 2, 3, 4, 5], dtype=tf.int64)
idx5b = tf.constant([[10], [20], [30], [40], [50]], dtype=tf.int64)
val5b = tf.constant([10, 20, 30, 40, 50], dtype=tf.int64)
cond0 = tf.constant([], dtype=bool)
cond5 = tf.constant([True, False, True, False, True], dtype=bool)
val3a = tf.constant([1, 2, 3], dtype=tf.int64)
val3b = tf.constant([4, 5, 6], dtype=tf.int64)
idx3c = tf.constant([[10], [20], [30]], dtype=tf.int64)
idx3d = tf.constant([[30], [40], [50]], dtype=tf.int64)
idx3e = tf.constant([[10], [30], [50]], dtype=tf.int64)
cond3 = tf.constant([True, False, True], dtype=bool)
shape = tf.constant([100], dtype=tf.int64)

# all inputs empty
(result_index, result_values,
 result_shape) = multiplex_3_op.examples_multiplex_sparse(
     idx0, cond0, shape, idx0, val0, shape, idx0, val0, shape)
self.assertAllEqual(idx0, result_index)
self.assertAllEqual(val0, result_values)
self.assertAllEqual(shape, result_shape)

# only b is not empty
(result_index, result_values,
 result_shape) = multiplex_3_op.examples_multiplex_sparse(
     idx0, cond0, shape, idx0, val0, shape, idx5b, val5a, shape)
self.assertAllEqual(idx5b, result_index)
self.assertAllEqual(val5a, result_values)
self.assertAllEqual(shape, result_shape)

# all indices the same
(result_index, result_values,
 result_shape) = multiplex_3_op.examples_multiplex_sparse(
     idx5b, cond5, shape, idx5b, val5a, shape, idx5b, val5b, shape)
expect_values = tf.constant([1, 20, 3, 40, 5], dtype=tf.int64)
self.assertAllEqual(idx5b, result_index)
self.assertAllEqual(expect_values, result_values)
self.assertAllEqual(shape, result_shape)

# cond and a have same positions, b values after a values
(result_index, result_values,
 result_shape) = multiplex_3_op.examples_multiplex_sparse(
     idx3c, cond3, shape, idx3c, val3a, shape, idx3d, val3b, shape)
expect_index = tf.constant([[10], [30], [40], [50]], dtype=tf.int64)
expect_values = tf.constant([1, 3, 5, 6], dtype=tf.int64)
self.assertAllEqual(expect_index, result_index)
self.assertAllEqual(expect_values, result_values)
self.assertAllEqual(shape, result_shape)

# cond and a have same positions, b values before a values
(result_index, result_values,
 result_shape) = multiplex_3_op.examples_multiplex_sparse(
     idx3d, cond3, shape, idx3d, val3a, shape, idx3c, val3b, shape)
expect_index = tf.constant([[10], [20], [30], [50]], dtype=tf.int64)
expect_values = tf.constant([4, 5, 1, 3], dtype=tf.int64)
self.assertAllEqual(expect_index, result_index)
self.assertAllEqual(expect_values, result_values)
self.assertAllEqual(shape, result_shape)

# cond and b have same positions, b values after a values
(result_index, result_values,
 result_shape) = multiplex_3_op.examples_multiplex_sparse(
     idx3d, cond3, shape, idx3c, val3a, shape, idx3d, val3b, shape)
expect_index = tf.constant([[30], [40]], dtype=tf.int64)
expect_values = tf.constant([3, 5], dtype=tf.int64)
self.assertAllEqual(expect_index, result_index)
self.assertAllEqual(expect_values, result_values)
self.assertAllEqual(shape, result_shape)

# cond and b have same positions, b values before a values
(result_index, result_values,
 result_shape) = multiplex_3_op.examples_multiplex_sparse(
     idx3c, cond3, shape, idx3d, val3a, shape, idx3c, val3b, shape)
expect_index = tf.constant([[20], [30]], dtype=tf.int64)
expect_values = tf.constant([5, 1], dtype=tf.int64)
self.assertAllEqual(expect_index, result_index)
self.assertAllEqual(expect_values, result_values)
self.assertAllEqual(shape, result_shape)

# cond and a and b all have different positions
(result_index, result_values,
 result_shape) = multiplex_3_op.examples_multiplex_sparse(
     idx3e, cond3, shape, idx3c, val3a, shape, idx3d, val3b, shape)
expect_index = tf.constant([[10], [30], [40]], dtype=tf.int64)
expect_values = tf.constant([1, 4, 5], dtype=tf.int64)
self.assertAllEqual(expect_index, result_index)
self.assertAllEqual(expect_values, result_values)
self.assertAllEqual(shape, result_shape)
