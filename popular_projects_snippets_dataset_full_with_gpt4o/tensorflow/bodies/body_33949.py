# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/stage_op_test.py
with ops.Graph().as_default() as G:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.int32, name='x')
        p = array_ops.placeholder(dtypes.int32, name='p')
    with ops.device(test.gpu_device_name()):
        stager = data_flow_ops.StagingArea(
            [
                dtypes.int32,
            ], shapes=[[]])
        stage = stager.put([x])
        peek = stager.peek(p)
        ret = stager.get()

G.finalize()

with self.session(graph=G) as sess:
    for i in range(10):
        sess.run(stage, feed_dict={x: i})

    for i in range(10):
        self.assertTrue(sess.run(peek, feed_dict={p: i}) == [i])
