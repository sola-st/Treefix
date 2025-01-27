# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stage_op_test.py
with ops.Graph().as_default() as G:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.float32, name='x')
        v = 2. * (array_ops.zeros([128, 128]) + x)
    with ops.device(test.gpu_device_name()):
        stager = data_flow_ops.StagingArea(
            [dtypes.float32, dtypes.float32],
            shapes=[[], [128, 128]],
            names=['x', 'v'])
        stage = stager.put({'x': x, 'v': v})
        ret = stager.get()
        size = stager.size()
        clear = stager.clear()

G.finalize()

with self.session(graph=G) as sess:
    sess.run(stage, feed_dict={x: -1})
    self.assertEqual(sess.run(size), 1)
    sess.run(stage, feed_dict={x: -1})
    self.assertEqual(sess.run(size), 2)
    sess.run(clear)
    self.assertEqual(sess.run(size), 0)
