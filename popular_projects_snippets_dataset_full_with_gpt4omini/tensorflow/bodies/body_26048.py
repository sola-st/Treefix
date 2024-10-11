# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
pb = dataset_options_pb2.ThreadingOptions()
if self.max_intra_op_parallelism is not None:
    pb.max_intra_op_parallelism = self.max_intra_op_parallelism
if self.private_threadpool_size is not None:
    pb.private_threadpool_size = self.private_threadpool_size
exit(pb)
