# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
# test low rank, like 5
for _ in range(5):
    self._RunAndVerifyResult(5, use_gpu=False)
for _ in range(5):
    self._RunAndVerifyResult(5, use_gpu=True)
# test high rank, like 10
for _ in range(5):
    self._RunAndVerifyResult(10, use_gpu=False)
for _ in range(5):
    self._RunAndVerifyResult(10, use_gpu=True)
