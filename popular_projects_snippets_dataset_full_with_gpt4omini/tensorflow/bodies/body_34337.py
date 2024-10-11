# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
with ops.Graph().as_default() as g:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.float32)
        f = array_ops.placeholder(dtypes.float32)
        v = array_ops.placeholder(dtypes.float32)
        pi = array_ops.placeholder(dtypes.int64)
        gi = array_ops.placeholder(dtypes.int64)
    with ops.device(test.gpu_device_name()):
        stager = data_flow_ops.MapStagingArea(
            [dtypes.float32, dtypes.float32, dtypes.float32])
        stage_xf = stager.put(pi, [x, f], [0, 2])
        stage_v = stager.put(pi, [v], [1])
        key, ret = stager.get(gi)
        size = stager.size()
        isize = stager.incomplete_size()

g.finalize()

with self.session(graph=g) as sess:
    # 0 complete and incomplete entries
    self.assertEqual(sess.run([size, isize]), [0, 0])
    # Stage key 0, x and f tuple entries
    sess.run(stage_xf, feed_dict={pi: 0, x: 1, f: 2})
    self.assertEqual(sess.run([size, isize]), [0, 1])
    # Stage key 1, x and f tuple entries
    sess.run(stage_xf, feed_dict={pi: 1, x: 1, f: 2})
    self.assertEqual(sess.run([size, isize]), [0, 2])

    # Now complete key 0 with tuple entry v
    sess.run(stage_v, feed_dict={pi: 0, v: 1})
    # 1 complete and 1 incomplete entry
    self.assertEqual(sess.run([size, isize]), [1, 1])
    # We can now obtain tuple associated with key 0
    self.assertEqual(sess.run([key, ret], feed_dict={gi: 0}), [0, [1, 1, 2]])

    # 0 complete and 1 incomplete entry
    self.assertEqual(sess.run([size, isize]), [0, 1])
    # Now complete key 1 with tuple entry v
    sess.run(stage_v, feed_dict={pi: 1, v: 3})
    # We can now obtain tuple associated with key 1
    self.assertEqual(sess.run([key, ret], feed_dict={gi: 1}), [1, [1, 3, 2]])
