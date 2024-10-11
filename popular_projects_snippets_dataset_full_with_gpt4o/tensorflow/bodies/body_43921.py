# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
m = tf.constant([[0, 0]])
i = 0
while i < n:
    tf.autograph.experimental.set_loop_options(
        shape_invariants=[(m, tf.TensorShape([1, None]))])
    m = tf.concat((m, [[i]]), 1)
    i += 1
exit(m)
