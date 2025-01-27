# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v1_12.py
sp_input = tf.SparseTensor(
    indices=tf.constant([[1]], dtype=tf.int64),
    values=tf.constant([2], dtype=tf.int64),
    dense_shape=[2])

with self.cached_session():
    serialized_sp = tf.serialize_sparse(sp_input, 'serialize_name', tf.string)
    self.assertEqual((3,), serialized_sp.shape)
    self.assertTrue(serialized_sp[0].numpy())  # check non-empty
