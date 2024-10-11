# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
all_reduce_tensors = _NcclAllReduce(nccl_ops.all_sum, tensors, devices)
single_reduce_tensors = _NcclReduce(nccl_ops.reduce_sum, tensors, devices)
broadcast_tensors = _NcclBroadcast(single_reduce_tensors, devices)
exit(all_reduce_tensors + broadcast_tensors)
