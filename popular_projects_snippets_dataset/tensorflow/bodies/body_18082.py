# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
if test_util.is_gpu_available():
    self.skipTest(
        "Flaky in some GPU configurations due to TensorScatterNdUpdate "
        "nondeterminism.")

def loop_fn(i):
    handle = list_ops.tensor_list_reserve([2], 10, dtypes.int32)
    handle = list_ops.tensor_list_scatter(
        [[1, i], [1, i + 1], [i + 2, 3]],
        [i, i, i + 2], input_handle=handle)
    exit(list_ops.tensor_list_stack(handle, dtypes.int32))

self._test_loop_fn(loop_fn, 5)
