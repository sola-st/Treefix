# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
import random

with ops.Graph().as_default() as g:
    with ops.device('/cpu:0'):
        x = array_ops.placeholder(dtypes.int32, name='x')
        pi = array_ops.placeholder(dtypes.int64, name='pi')
        gi = array_ops.placeholder(dtypes.int64, name='gi')
    with ops.device(test.gpu_device_name()):
        stager = data_flow_ops.MapStagingArea([
            dtypes.int32,
        ],
                                              shapes=[[]],
                                              ordered=True)
        stage = stager.put(pi, [x], [0])
        get = stager.get()
        size = stager.size()

g.finalize()

n = 10

with self.session(graph=g) as sess:
    # Keys n-1..0
    keys = list(reversed(range(n)))

    for i in keys:
        sess.run(stage, feed_dict={pi: i, x: i})

    self.assertEqual(sess.run(size), n)

    # Check that key, values come out in ascending order
    for i, k in enumerate(reversed(keys)):
        get_key, values = sess.run(get)
        self.assertTrue(i == k == get_key == values)

    self.assertEqual(sess.run(size), 0)
