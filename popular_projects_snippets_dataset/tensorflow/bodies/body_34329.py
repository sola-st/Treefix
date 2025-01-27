# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
with ops.Graph().as_default() as g:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.int32, name='x')
        pi = array_ops.placeholder(dtypes.int64)
        gi = array_ops.placeholder(dtypes.int64)
        p = array_ops.placeholder(dtypes.int32, name='p')
    with ops.device(test.gpu_device_name()):
        stager = data_flow_ops.MapStagingArea([
            dtypes.int32,
        ], shapes=[[]])
        stage = stager.put(pi, [x], [0])
        peek = stager.peek(gi)
        size = stager.size()

g.finalize()

n = 10

with self.session(graph=g) as sess:
    for i in range(n):
        sess.run(stage, feed_dict={x: i, pi: i})

    for i in range(n):
        self.assertEqual(sess.run(peek, feed_dict={gi: i})[0], i)

    self.assertEqual(sess.run(size), 10)
