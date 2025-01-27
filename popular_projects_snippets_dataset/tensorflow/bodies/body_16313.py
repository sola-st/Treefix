# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
self._Test(partial(_NcclAllReduce, nccl_ops.all_sum), lambda x, y: x + y)
self._Test(partial(_NcclAllReduce, nccl_ops.all_prod), lambda x, y: x * y)
self._Test(partial(_NcclAllReduce, nccl_ops.all_min), np.minimum)
self._Test(partial(_NcclAllReduce, nccl_ops.all_max), np.maximum)
