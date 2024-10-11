# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
m = tf.constant([[0]])
for i in l:
    tf.autograph.experimental.set_loop_options(
        shape_invariants=[(m, tf.TensorShape([None, 1]))])
    m = tf.concat((m, [[i]]), 0)
exit(m)
