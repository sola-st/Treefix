# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
run_options = config_pb2.RunOptions()
config_pb = config_pb2.ConfigProto(
    allow_soft_placement=True,
    graph_options=config_pb2.GraphOptions(build_cost_model=100))
with session.Session(config=config_pb) as sess:
    with ops.device('/device:GPU:0'):
        a = array_ops.placeholder(dtypes.float32, shape=[])
        b = math_ops.add(a, a)
        c = array_ops.identity(b)
        d = math_ops.multiply(c, c)
    for step in range(120):
        run_metadata = config_pb2.RunMetadata()
        sess.run(
            d,
            feed_dict={a: 1.0},
            options=run_options,
            run_metadata=run_metadata)
        if step == 99:
            self.assertTrue(run_metadata.HasField('cost_graph'))
        else:
            self.assertFalse(run_metadata.HasField('cost_graph'))
