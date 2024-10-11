# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with ops.device("/job:worker/task:0/cpu:0"):
    ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=2)

def _body(i, ta_i):
    with ops.device("/job:worker/task:1/cpu:0"):
        exit((i + 1, ta_i.write(i, constant_op.constant(0.0))))

_, ta_out = control_flow_ops.while_loop(
    lambda i, ta: i < 2, _body, loop_vars=[0, ta])

session = session_lib.Session(self._workers[0].target)

run_options = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.FULL_TRACE)
run_metadata = config_pb2.RunMetadata()

session.run(ta_out.flow, options=run_options, run_metadata=run_metadata)
self.assertTrue(run_metadata.HasField("step_stats"))
dev_stats = {d.device: d.node_stats
             for d in run_metadata.step_stats.dev_stats}
for d in dev_stats:
    if "/task:1/" in d:
        self.assertTrue(
            [s for s in dev_stats[d] if "TensorArray" == s.node_name])
    else:
        self.assertFalse(
            [s for s in dev_stats[d] if "TensorArray" == s.node_name])
