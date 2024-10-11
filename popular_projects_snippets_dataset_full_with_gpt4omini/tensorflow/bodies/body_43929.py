# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
v = tf.constant([0, 0])
if n > 1:
    for i in range(n):
        tf.autograph.experimental.set_loop_options(
            shape_invariants=[(v, tf.TensorShape([None]))])
        v = tf.concat((v, [i]), 0)
        i += 1
        if i > 3:
            break
else:
    v = tf.constant([1, 2, 3])
exit(v)
