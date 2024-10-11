# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_stage_op_test.py
with ops.Graph().as_default() as g:
    x = array_ops.placeholder(dtypes.float32)
    v = 2. * (array_ops.zeros([128, 128]) + x)
    t = data_flow_ops.gen_data_flow_ops.map_stage(
        key=constant_op.constant(value=[1], shape=(1, 3), dtype=dtypes.int64),
        indices=np.array([[6]]),
        values=[x, v],
        dtypes=[dtypes.int64],
        capacity=0,
        memory_limit=0,
        container='container1',
        shared_name='',
        name=None)

g.finalize()

with self.session(graph=g) as sess:
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                'key must be an int64 scalar'):
        sess.run(t, feed_dict={x: 1})
