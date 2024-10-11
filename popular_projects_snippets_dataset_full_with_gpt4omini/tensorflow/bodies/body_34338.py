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
        # Test barrier with dictionary
        stager = data_flow_ops.MapStagingArea(
            [dtypes.float32, dtypes.float32, dtypes.float32],
            names=['x', 'v', 'f'])
        stage_xf = stager.put(pi, {'x': x, 'f': f})
        stage_v = stager.put(pi, {'v': v})
        peek_xf = stager.peek(pei, ['x', 'f'])
        peek_v = stager.peek(pei, ['v'])
        key_xf, get_xf = stager.get(gi, ['x', 'f'])
        key_v, get_v = stager.get(gi, ['v'])
        pop_key_xf, pop_xf = stager.get(indices=['x', 'f'])
        pop_key_v, pop_v = stager.get(pi, ['v'])
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

    # We can now peek at 'x' and 'f' values associated with key 0
    self.assertEqual(sess.run(peek_xf, feed_dict={pei: 0}), {'x': 1, 'f': 2})
    # Peek at 'v' value associated with key 0
    self.assertEqual(sess.run(peek_v, feed_dict={pei: 0}), {'v': 1})
    # 1 complete and 1 incomplete entry
    self.assertEqual(sess.run([size, isize]), [1, 1])

    # We can now obtain 'x' and 'f' values associated with key 0
    self.assertEqual(
        sess.run([key_xf, get_xf], feed_dict={gi: 0}), [0, {
            'x': 1,
            'f': 2
        }])
    # Still have 1 complete and 1 incomplete entry
    self.assertEqual(sess.run([size, isize]), [1, 1])

    # We can no longer get 'x' and 'f' from key 0
    with self.assertRaises(errors.InvalidArgumentError) as cm:
        sess.run([key_xf, get_xf], feed_dict={gi: 0})

    exc_str = ("Tensor at index '0' for key '0' " 'has already been removed.')

    self.assertIn(exc_str, cm.exception.message)

    # Obtain 'v' value associated with key 0
    self.assertEqual(
        sess.run([key_v, get_v], feed_dict={gi: 0}), [0, {
            'v': 1
        }])
    # 0 complete and 1 incomplete entry
    self.assertEqual(sess.run([size, isize]), [0, 1])

    # Now complete key 1 with tuple entry v
    sess.run(stage_v, feed_dict={pi: 1, v: 1})
    # 1 complete and 1 incomplete entry
    self.assertEqual(sess.run([size, isize]), [1, 0])

    # Pop without key to obtain 'x' and 'f' values associated with key 1
    self.assertEqual(sess.run([pop_key_xf, pop_xf]), [1, {'x': 1, 'f': 2}])
    # still 1 complete and 1 incomplete entry
    self.assertEqual(sess.run([size, isize]), [1, 0])
    # We can now obtain 'x' and 'f' values associated with key 1
    self.assertEqual(
        sess.run([pop_key_v, pop_v], feed_dict={pi: 1}), [1, {
            'v': 1
        }])
    # Nothing is left
    self.assertEqual(sess.run([size, isize]), [0, 0])
