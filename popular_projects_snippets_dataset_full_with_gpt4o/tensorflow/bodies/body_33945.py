# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stage_op_test.py
with ops.Graph().as_default() as G:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.float32)
        v = 2. * (array_ops.zeros([128, 128]) + x)
    with ops.device(test.gpu_device_name()):
        stager = data_flow_ops.StagingArea([dtypes.float32])
        stage = stager.put([v])
        y = stager.get()
        y = math_ops.reduce_max(math_ops.matmul(y, y))

G.finalize()

with self.session(graph=G) as sess:
    sess.run(stage, feed_dict={x: -1})
    for i in range(10):
        _, yval = sess.run([stage, y], feed_dict={x: i})
        self.assertAllClose(4 * (i - 1) * (i - 1) * 128, yval, rtol=1e-4)
