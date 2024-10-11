# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
group_key = 1
instance_key = 1
with self.session(
    config=config_pb2.ConfigProto(device_count={'CPU': 2})) as sess:
    with ops.device('/CPU:0'):
        in0 = constant_op.constant(t0)
        c0 = collective_ops.all_gather(in0, 2, group_key, instance_key)
    with ops.device('/CPU:1'):
        in1 = constant_op.constant(t1)
        c1 = collective_ops.all_gather(in1, 2, group_key, instance_key)
    run_options = config_pb2.RunOptions()
    if set_graph_key:
        run_options.experimental.collective_graph_key = 1
    results = sess.run([c0, c1], options=run_options)
self.assertAllClose(results[0], expected, rtol=1e-5, atol=1e-5)
self.assertAllClose(results[1], expected, rtol=1e-5, atol=1e-5)
