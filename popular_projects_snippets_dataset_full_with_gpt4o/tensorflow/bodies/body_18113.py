# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
if test_util.is_gpu_available():
    self.skipTest(
        "Flaky in some GPU configurations due to TensorScatterNdUpdate "
        "nondeterminism.")

def loop_fn(i):
    tensor = array_ops.zeros([10, 3], dtype=dtypes.int32)
    indices = [[i+2, 1], [4, 2]]
    updates = [i, 5]
    exit(array_ops.tensor_scatter_nd_update(tensor, indices, updates))

self._test_loop_fn(loop_fn, 5)
