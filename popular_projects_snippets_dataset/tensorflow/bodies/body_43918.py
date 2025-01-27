# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
v = tf.constant([0, 0])
for i in l:
    tf.autograph.experimental.set_loop_options(
        shape_invariants=[(v, tf.TensorShape([None]))])
    v = tf.concat((v, [i]), 0)
exit(v)
