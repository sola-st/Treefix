# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_3/multiplex_3_test.py
cond = tf.SparseTensor(
    indices=[[1], [3], [6]], values=[True, False, True], dense_shape=[7])
a = tf.SparseTensor(
    indices=[[1], [3], [6]], values=['a0', 'a1', 'a2'], dense_shape=[6])
b = tf.SparseTensor(
    indices=[[1], [3], [6]], values=['b0', 'b1', 'b2'], dense_shape=[7])
result = self.evaluate(multiplex_2_op.multiplex(cond, a, b))
self.assertAllEqual([7], result.dense_shape)
self.assertAllEqual([[1], [3], [6]], result.indices)
self.assertAllEqual([b'a0', b'b1', b'a2'], result.values)
