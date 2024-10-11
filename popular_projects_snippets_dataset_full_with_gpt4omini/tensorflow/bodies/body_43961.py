# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_illegal_cases_test.py
t = tf.constant([1])
for _ in l:
    tf.autograph.experimental.set_loop_options(
        shape_invariants=((t, tf.TensorShape([1])),))
    t = tf.range(tf.random.uniform((), 2, 3, dtype=tf.int32))
exit(t)
