# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
with ops.Graph().as_default() as g:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.float32)
        pi = array_ops.placeholder(dtypes.int64)
        gi = array_ops.placeholder(dtypes.int64)
        v = 2. * (array_ops.zeros([128, 128]) + x)
    with ops.device(test.gpu_device_name()):
        stager = data_flow_ops.MapStagingArea([dtypes.float32])
        stage = stager.put(pi, [v], [0])
        k, y = stager.get(gi)
        y = math_ops.reduce_max(math_ops.matmul(y, y))

g.finalize()

with self.session(graph=g) as sess:
    sess.run(stage, feed_dict={x: -1, pi: 0})
    for i in range(10):
        _, yval = sess.run([stage, y], feed_dict={x: i, pi: i + 1, gi: i})
        self.assertAllClose(4 * (i - 1) * (i - 1) * 128, yval, rtol=1e-4)
