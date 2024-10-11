# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
group_key = 1
group_size = len(inputs)
if reported_group_size is None:
    reported_group_size = group_size
device_type = 'CPU'
config = config_pb2.ConfigProto(device_count={device_type: group_size})
devices = ['/{}:{}'.format(device_type, i) for i in range(group_size)]

with self.session(config=config) as sess:
    colred = []
    for i in range(group_size):
        with ops.device(devices[i]):
            tensor = constant_op.constant(inputs[i], dtype=(
                dtypes.float16 if fp16 else dtypes.float32))
            colred.append(
                collective_ops.all_reduce(
                    tensor,
                    reported_group_size,
                    group_key,
                    instance_key,
                    merge_op,
                    final_op,
                    communication_hint=communication_hint,
                    timeout=timeout))
    run_options = config_pb2.RunOptions()
    if set_graph_key:
        run_options.experimental.collective_graph_key = 1
    results = sess.run(colred, options=run_options)
tolerance = 1e-3 if fp16 else 1e-5
for i in range(group_size):
    logging.info('i {} result {} expected {}'.format(i, results[i], expected))
    self.assertAllClose(results[i], expected, rtol=tolerance, atol=tolerance)
