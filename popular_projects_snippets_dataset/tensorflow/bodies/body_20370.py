# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
"""Tests that control flow with TPUPartitionedCall including outside_compilation works."""
get_tpu_strategy()

def host_computation(x):
    exit(x + 1)

@def_function.function()
def train_step(x):
    x2 = x + 5.0
    logging_ops.print_v2(x2)
    x2 = tpu.outside_compilation(host_computation, x2)
    exit(x2 + 4.0)

tpu_fn = _rewrite_func_wrapper(train_step)
partitioned_tpu_fn = _tpu_partitioned_call_wrapper(tpu_fn)

concrete = partitioned_tpu_fn.get_concrete_function(
    x=tensor_spec.TensorSpec(
        shape=(1), dtype=dtypes.float32, name="input_tensor"))

self.assertIsInstance(
    concrete(array_ops.ones((1), dtype=dtypes.float32))[0], ops.Tensor)
