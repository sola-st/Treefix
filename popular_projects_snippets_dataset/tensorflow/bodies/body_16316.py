# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
self._Test(partial(_NcclReduce, nccl_ops.reduce_sum), lambda x, y: x + y)
