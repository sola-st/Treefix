# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
# Broadcasts on a single device are removed completely during rewrite.
self._Test(_NcclBroadcast, lambda x, y: x,
           (['/device:GPU:0', '/device:GPU:0'],))
