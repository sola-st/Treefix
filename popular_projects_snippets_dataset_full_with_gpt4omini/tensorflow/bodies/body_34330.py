# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
with ops.Graph().as_default() as g:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.float32, name='x')
        pi = array_ops.placeholder(dtypes.int64)
        gi = array_ops.placeholder(dtypes.int64)
        v = 2. * (array_ops.zeros([128, 128]) + x)
    with ops.device(test.gpu_device_name()):
        stager = data_flow_ops.MapStagingArea([dtypes.float32, dtypes.float32],
                                              shapes=[[], [128, 128]],
                                              names=['x', 'v'])
        stage = stager.put(pi, {'x': x, 'v': v})
        size = stager.size()
        clear = stager.clear()

g.finalize()

with self.session(graph=g) as sess:
    sess.run(stage, feed_dict={x: -1, pi: 3})
    self.assertEqual(sess.run(size), 1)
    sess.run(stage, feed_dict={x: -1, pi: 1})
    self.assertEqual(sess.run(size), 2)
    sess.run(clear)
    self.assertEqual(sess.run(size), 0)
