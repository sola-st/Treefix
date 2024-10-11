# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
v = tf.SparseTensor(
    indices=[[0, 0], [1, 1]], values=[1, 2], dense_shape=[3, 3])
i = 0
while i < n:
    tf.autograph.experimental.set_loop_options(
        shape_invariants=[(v, tf.TensorShape(None))])
    v = tf.sparse.expand_dims(v)
    i += 1
exit(v)
