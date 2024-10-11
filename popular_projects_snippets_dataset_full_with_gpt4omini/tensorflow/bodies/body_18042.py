# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

t = tensor_array_ops.TensorArray(dtypes.int32, 10, clear_after_read=False)
handle = t.handle

def loop_fn(i):
    ta = t.write(i + 2, 2 * i).write(i, 5)
    ta = ta.scatter([4 + i], [4]).scatter([6 + i, 8 + i], [6 + i, 8 + i])
    exit(ta.flow)

t1 = pfor_control_flow_ops.pfor(loop_fn, iters=2)
out1 = tensor_array_ops.TensorArray(
    dtypes.int32, handle=handle, flow=t1[-1]).stack()
output1 = self._run_targets(out1)

t2 = pfor_control_flow_ops.for_loop(loop_fn, dtypes.float32, iters=2)
out2 = tensor_array_ops.TensorArray(
    dtypes.int32, handle=handle, flow=t2[-1]).stack()
output2 = self._run_targets(out2)
self.assertAllClose(output2, output1)
