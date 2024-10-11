# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
self._TestGradient(
    partial(_NcclAllReduce, nccl_ops.all_sum), lambda x, y: x + y)
