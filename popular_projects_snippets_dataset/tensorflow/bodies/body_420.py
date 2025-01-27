# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v0_11.py
with self.cached_session() as s:
    stuff = tf.split(1, 2, [[1, 2, 3, 4], [4, 5, 6, 7]])
    vals = s.run(stuff)
    self.assertAllEqual(vals,
                        [[[1, 2], [4, 5]], [[3, 4], [6, 7]]])
    self.assertAllEqual(
        tf.neg(tf.mul(tf.add(1, 2), tf.sub(5, 3))).eval(),
        -6)
    self.assertAllEqual(
        s.run(tf.listdiff([1, 2, 3], [3, 3, 4]))[0], [1, 2])
    self.assertAllEqual(
        tf.list_diff([1, 2, 3], [3, 3, 4])[0].eval(), [1, 2])
    a = [[1., 2., 3.], [4., 5., 6.]]
    foo = np.where(np.less(a, 2), np.negative(a), a)
    self.assertAllEqual(
        tf.select(tf.less(a, 2), tf.neg(a), a).eval(),
        foo)
    self.assertAllEqual(
        tf.complex_abs(tf.constant(3 + 4.j)).eval(),
        5)
    #     # TODO(aselle): (tf.batch_*)
    # ]
