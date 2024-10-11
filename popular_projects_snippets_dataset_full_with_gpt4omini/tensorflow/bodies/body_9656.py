# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session() as s:
    x = array_ops.zeros([2])

    y = s.run(2 * x, feed_dict={x: np.ones(2).astype(np.float32)})
    self.assertAllEqual(y, 2 * np.ones(2))

    y = s.run(2 * x, feed_dict={x.name: np.ones(2).astype(np.float32)})
    self.assertAllEqual(y, 2 * np.ones(2))

    y = s.run(2 * x, feed_dict={x: [1, 1]})
    assert (y == 2 * np.ones(2)).all()

    # Test nested tuple keys
    z = (((array_ops.zeros([2]),),), array_ops.zeros([2]),
         (array_ops.zeros([2]),))
    result = [z[0][0][0] * 2, z[1] * 2, z[2][0] * 2]
    values = (((np.array([1, 1]),),), np.array([2, 2]), (np.array([3, 3]),))
    result_value = s.run(result, feed_dict={z: values})
    self.assertAllEqual(result_value[0], 2 * np.ones(2))
    self.assertAllEqual(result_value[1], 2 * np.array([2, 2]))
    self.assertAllEqual(result_value[2], 2 * np.array([3, 3]))
