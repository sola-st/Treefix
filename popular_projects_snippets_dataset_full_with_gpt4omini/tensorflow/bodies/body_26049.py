# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
if pb.WhichOneof("optional_max_intra_op_parallelism") is not None:
    self.max_intra_op_parallelism = pb.max_intra_op_parallelism
if pb.WhichOneof("optional_private_threadpool_size") is not None:
    self.private_threadpool_size = pb.private_threadpool_size
