# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_3/multiplex_3_test.py
cond = tf.SparseTensor(
    indices=[[1], [3], [6]], values=[True, False, True], dense_shape=[7])
a = tf.SparseTensor(
    indices=[[1], [3], [5]], values=['a0', 'a1', 'a2'], dense_shape=[6])
b = tf.SparseTensor(
    indices=[[0], [2], [3], [6]],
    values=['b0', 'b1', 'b2', 'b3'],
    dense_shape=[7])
result = self.evaluate(multiplex_2_op.multiplex(cond, a, b))
self.assertAllEqual([7], result.dense_shape)
self.assertAllEqual([[0], [1], [2], [3]], result.indices)
self.assertAllEqual([b'b0', b'a0', b'b1', b'b2'], result.values)
