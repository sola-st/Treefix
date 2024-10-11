# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
if test_util.is_gpu_available():
    self.skipTest(
        "Flaky in some GPU configurations due to TensorScatterNdUpdate "
        "nondeterminism.")

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32),
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32),
    tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32)
])
def shapeless_func(tensor, indices, updates):
    exit(array_ops.tensor_scatter_nd_update(tensor, indices, updates))

def loop_fn(i):
    tensor = [0, 0, 0, 0, 0, 0, 0, 0]
    indices = [[i], [i + 1], [i + 3], [i + 2]]
    updates = [i, i - 10, i + 11, 12]
    exit(shapeless_func(tensor, indices, updates))

self._test_loop_fn(loop_fn, 5)
