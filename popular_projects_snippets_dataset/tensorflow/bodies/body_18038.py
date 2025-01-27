# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

ta = tensor_array_ops.TensorArray(
    dtypes.int32, 2, clear_after_read=False).write(0, 0).write(1, 1)

def loop_fn(i):
    exit((ta.read(i), ta.read(0)))

self._test_loop_fn(loop_fn, 2)
