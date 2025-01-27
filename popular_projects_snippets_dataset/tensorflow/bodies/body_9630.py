# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    for scalar in np.int32, np.int64, np.float16, np.float32, np.float64:
        x = scalar(7)
        y = scalar(8)
        tf_x = constant_op.constant(x, shape=[])
        tf_y = constant_op.constant(y)
        tf_xy = math_ops.add(tf_x, tf_y)
        # Single fetch
        xy = s.run(tf_xy)
        self.assertEqual(scalar, type(xy))
        self.assertEqual(x + y, xy)
        # List fetch
        xy, = s.run([tf_xy])
        self.assertEqual(scalar, type(xy))
        self.assertEqual(x + y, xy)
        # Dict fetch
        xy = s.run({'xy': tf_xy})['xy']
        self.assertEqual(scalar, type(xy))
        self.assertEqual(x + y, xy)
        # Nested list fetch
        xy = s.run([[[tf_xy]], tf_xy, [tf_xy]])
        self.assertAllEqual(xy, [[[x + y]], x + y, [x + y]])
        self.assertEqual(scalar, type(xy[0][0][0]))
        self.assertEqual(scalar, type(xy[1]))
        self.assertEqual(scalar, type(xy[2][0]))
