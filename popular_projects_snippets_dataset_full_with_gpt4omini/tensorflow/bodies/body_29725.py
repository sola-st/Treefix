# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/large_concat_op_test.py
# CPU-only test, because it fails on GPUs with <= 4GB memory.
with ops.device("/cpu:0"):
    a = array_ops.ones([2**31 + 6], dtype=dtypes.int8)
    b = array_ops.zeros([1024], dtype=dtypes.int8)
    onezeros = array_ops.concat([a, b], 0)
with self.session(use_gpu=False):
    # TODO(dga):  Add more depth to this test to validate correctness,
    # not just non-crashingness, once other large tensor fixes have gone in.
    _ = self.evaluate(onezeros)
