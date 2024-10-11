# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with ops.device("/job:worker/task:0/cpu:0"):
    # this initial device will be ignored.
    ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=2)
with ops.device("/job:worker/task:1/cpu:0"):
    # the first write sets the op's device.
    ta = ta.write(0, 1.0)
with ops.device("/job:worker/task:2/cpu:0"):
    # subsequent writes do not modify the op's device.
    ta = ta.write(1, 1.0)

# The gradient TA will sit on the same device as the forward TA.
ta_grad = ta.grad("grad")
flows = [ta.flow, ta_grad.flow]

# Similar tests for unpack and split
with ops.device("/job:worker/task:0/cpu:0"):
    ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=3)
with ops.device("/job:worker/task:1/cpu:0"):
    ta = ta.unstack([1.0, 2.0])
with ops.device("/job:worker/task:2/cpu:0"):
    ta = ta.write(2, 3.0)
flows.append(ta.flow)

with ops.device("/job:worker/task:0/cpu:0"):
    ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=2)
with ops.device("/job:worker/task:1/cpu:0"):
    ta = ta.split([1.0, 2.0], [1, 1])
flows.append(ta.flow)

session = session_lib.Session(self._workers[0].target)

run_options = config_pb2.RunOptions(
    trace_level=config_pb2.RunOptions.FULL_TRACE)
run_metadata = config_pb2.RunMetadata()

session.run(flows, options=run_options, run_metadata=run_metadata)
self.assertTrue(run_metadata.HasField("step_stats"))
dev_stats = {d.device: d.node_stats
             for d in run_metadata.step_stats.dev_stats}
for d in dev_stats:
    if "/task:1/" in d:
        self.assertTrue(
            [s for s in dev_stats[d] if "/TensorArray" in s.node_name])
    elif "/host:CPU" not in d:
        self.assertFalse(
            [s for s in dev_stats[d] if "/TensorArray" in s.node_name])
