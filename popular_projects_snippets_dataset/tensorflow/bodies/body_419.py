# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v0_11.py
with self.cached_session():

    # TODO(aselle): sparse_split, sparse_reduce_sum,
    #  sparse_reduce_sum_sparse, reduce_join
    a = [[1, 2, 3]]
    self.assertAllEqual(tf.expand_dims(tf.squeeze(a, [0]), 0).eval(),
                        a)
    self.assertAllEqual(tf.squeeze(tf.expand_dims(a, 1), [1]).eval(),
                        a)
    self.assertAllEqual(
        tf.expand_dims(tf.squeeze([[1, 2, 3]], axis=[0]), dim=0).eval(), a)
    self.assertAllEqual(
        tf.squeeze(tf.expand_dims([[1, 2, 3]], dim=1), axis=[1]).eval(), a)

    self.assertAllEqual(
        tf.squeeze(tf.expand_dims([[1, 2, 3]], dim=1), axis=[1]).eval(), a)
