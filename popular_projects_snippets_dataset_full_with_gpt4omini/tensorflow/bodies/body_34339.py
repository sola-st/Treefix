# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
with ops.Graph().as_default() as g:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.float32)
        f = array_ops.placeholder(dtypes.float32)
        v = array_ops.placeholder(dtypes.float32)
        pi = array_ops.placeholder(dtypes.int64)
        pei = array_ops.placeholder(dtypes.int64)
        gi = array_ops.placeholder(dtypes.int64)
    with ops.device(test.gpu_device_name()):
        # Test again with partial index gets
        stager = data_flow_ops.MapStagingArea(
            [dtypes.float32, dtypes.float32, dtypes.float32])
        stage_xvf = stager.put(pi, [x, v, f], [0, 1, 2])
        key_xf, get_xf = stager.get(gi, [0, 2])
        key_v, get_v = stager.get(gi, [1])
        size = stager.size()
        isize = stager.incomplete_size()

g.finalize()

with self.session(graph=g) as sess:
    # Stage complete tuple
    sess.run(stage_xvf, feed_dict={pi: 0, x: 1, f: 2, v: 3})

    self.assertEqual(sess.run([size, isize]), [1, 0])

    # Partial get using indices
    self.assertEqual(
        sess.run([key_xf, get_xf], feed_dict={gi: 0}), [0, [1, 2]])

    # Still some of key 0 left
    self.assertEqual(sess.run([size, isize]), [1, 0])

    # Partial get of remaining index
    self.assertEqual(sess.run([key_v, get_v], feed_dict={gi: 0}), [0, [3]])

    # All gone
    self.assertEqual(sess.run([size, isize]), [0, 0])
