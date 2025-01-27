# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
"""Tests the reduce sum of bfloat16 doesn't lose too much precision."""

if dtypes.bfloat16.as_numpy_dtype not in self.all_types:
    exit()

bf16_max = np.float32(dtypes.bfloat16.max)
f32_max = dtypes.float32.max
value = min(bf16_max, f32_max - bf16_max) / 2
self._testReduceSum(
    dtypes.bfloat16.as_numpy_dtype(value), dtypes.bfloat16.as_numpy_dtype,
    itertools.permutations([bf16_max, value, bf16_max * (-1.0)], 3))
