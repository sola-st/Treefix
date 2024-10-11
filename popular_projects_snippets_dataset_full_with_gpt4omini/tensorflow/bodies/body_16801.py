# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
group_key = 1
instance_key = 1
with self.session(
    config=config_pb2.ConfigProto(device_count={'CPU': 2})) as sess:
    with ops.device('/CPU:0'):
        in0 = constant_op.constant(in_val)
        out0 = collective_ops.broadcast_send(in0, in0.shape, in0.dtype,
                                             2, group_key, instance_key)
    with ops.device('/CPU:1'):
        c1 = constant_op.constant(in_val)
        out1 = collective_ops.broadcast_recv(c1.shape, c1.dtype,
                                             2, group_key, instance_key)
    run_options = config_pb2.RunOptions()
    run_options.experimental.collective_graph_key = 1
    results = sess.run([out0, out1], options=run_options)
self.assertAllClose(results[0], in_val, rtol=1e-5, atol=1e-5)
self.assertAllClose(results[1], in_val, rtol=1e-5, atol=1e-5)
