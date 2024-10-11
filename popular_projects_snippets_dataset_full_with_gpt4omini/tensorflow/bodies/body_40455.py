# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with ops.Graph().as_default():
    with backprop.GradientTape() as tape:
        a = array_ops.placeholder(dtype=dtypes.float32, shape=None)
        tape.watch(a)
        b = a**3

    db_da = tape.gradient(b, a)

    with self.cached_session() as sess:
        self.assertEqual((8.0, 12.0), sess.run((b, db_da), feed_dict={a: 2.0}))
