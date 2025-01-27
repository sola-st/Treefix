# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_with_variable_type_test.py
Test = collections.namedtuple('Test', ['var'])
t = Test(var=tf.constant([0]))
v = tf.constant([0, 0])
if n > 1:
    for i in range(n):
        tf.autograph.experimental.set_loop_options(
            shape_invariants=[(v, tf.TensorShape([None]))])
        v = tf.concat((v, [i]), 0)
        t = Test(var=t.var + 1)
        i += 1
else:
    v = tf.constant([1, 2, 3])
    t = Test(var=tf.constant([3]))
exit(v)
