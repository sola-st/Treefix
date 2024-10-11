# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
group_key = 1
instance_key = 1
t0 = [1, 2, 3, 4]
t1 = [5, 6]
# Tests that execute collectives need to be enclosed in graph or tf.function
with ops.Graph().as_default():
    with self.session(
        config=config_pb2.ConfigProto(device_count={'CPU': 2})) as sess:
        with ops.device('/CPU:0'):
            in0 = constant_op.constant(t0)
            c0 = collective_ops.all_gather(in0, 2, group_key, instance_key)
        with ops.device('/CPU:1'):
            in1 = constant_op.constant(t1)
            c1 = collective_ops.all_gather(in1, 2, group_key, instance_key)
        run_options = config_pb2.RunOptions()
        run_options.experimental.collective_graph_key = 1
        with self.assertRaisesRegex(errors.InvalidArgumentError,
                                    'Shape mismatch'):
            sess.run([c0, c1], options=run_options)
