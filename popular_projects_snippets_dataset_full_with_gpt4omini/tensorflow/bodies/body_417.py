# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v0_11.py
with self.cached_session():

    a = [[1., 2., 3.], [4., 5., 6.]]
    b = [[True, False, False], [False, True, True]]
    dim0 = [1]
    dim1 = [1]

    self.assertAllEqual(
        tf.reduce_any(
            b, reduction_indices=dim0).eval(), [True, True])
    self.assertAllEqual(
        tf.reduce_all(
            b, reduction_indices=[0]).eval(), [False, False, False])
    self.assertAllEqual(
        tf.reduce_all(
            b, reduction_indices=dim1).eval(), [False, False])
    self.assertAllEqual(
        tf.reduce_sum(
            a, reduction_indices=[1]).eval(), [6., 15.])
    self.assertAllEqual(
        tf.reduce_sum(
            a, reduction_indices=[0, 1]).eval(), 21.0)
    self.assertAllEqual(tf.reduce_sum(a, [0, 1]).eval(), 21.0)
    self.assertAllEqual(
        tf.reduce_prod(
            a, reduction_indices=[1]).eval(), [6., 120.])
    self.assertAllEqual(
        tf.reduce_prod(
            a, reduction_indices=[0, 1]).eval(), 720.0)
    self.assertAllEqual(tf.reduce_prod(a, [0, 1]).eval(), 720.0)
    self.assertAllEqual(
        tf.reduce_mean(
            a, reduction_indices=[1]).eval(), [2., 5.])
    self.assertAllEqual(
        tf.reduce_mean(
            a, reduction_indices=[0, 1]).eval(), 3.5)
    self.assertAllEqual(tf.reduce_mean(a, [0, 1]).eval(), 3.5)
    self.assertAllEqual(
        tf.reduce_min(
            a, reduction_indices=[1]).eval(), [1., 4.])
    self.assertAllEqual(
        tf.reduce_min(
            a, reduction_indices=[0, 1]).eval(), 1.0)
    self.assertAllEqual(tf.reduce_min(a, [0, 1]).eval(), 1.0)
    self.assertAllEqual(
        tf.reduce_max(
            a, reduction_indices=[1]).eval(), [3., 6.])
    self.assertAllEqual(
        tf.reduce_max(
            a, reduction_indices=[0, 1]).eval(), 6.0)
    self.assertAllEqual(tf.reduce_max(a, [0, 1]).eval(), 6.0)
    self.assertAllClose(tf.reduce_logsumexp(a, reduction_indices=[1]).eval(),
                        [3.40760589, 6.40760612])
    self.assertAllClose(
        tf.reduce_logsumexp(a, reduction_indices=[0, 1]).eval(),
        6.45619344711)
    self.assertAllClose(
        tf.reduce_logsumexp(a, [0, 1]).eval(), 6.45619344711)
    self.assertAllEqual(
        tf.expand_dims([[1, 2], [3, 4]], axis=1).eval(),
        [[[1, 2]], [[3, 4]]])
