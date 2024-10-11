# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
m = tf.constant([[0, 0], [0, 0]])
i = 0
while i < n:
    tf.autograph.experimental.set_loop_options(
        shape_invariants=[(m, tf.TensorShape(None))])
    m = tf.pad(m, [[1, 1], [1, 1]], constant_values=i)
    i += 1
exit(m)
