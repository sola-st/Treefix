# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
pb = dataset_options_pb2.OptimizationOptions()
if self.apply_default_optimizations is not None:
    pb.apply_default_optimizations = self.apply_default_optimizations
if self.filter_fusion is not None:
    pb.filter_fusion = self.filter_fusion
if self.filter_parallelization is not None:
    pb.filter_parallelization = self.filter_parallelization
if self.inject_prefetch is not None:
    pb.inject_prefetch = self.inject_prefetch
if self.map_and_batch_fusion is not None:
    pb.map_and_batch_fusion = self.map_and_batch_fusion
if self.map_and_filter_fusion is not None:
    pb.map_and_filter_fusion = self.map_and_filter_fusion
if self.map_fusion is not None:
    pb.map_fusion = self.map_fusion
if self.map_parallelization is not None:
    pb.map_parallelization = self.map_parallelization
if self.noop_elimination is not None:
    pb.noop_elimination = self.noop_elimination
if self.parallel_batch is not None:
    pb.parallel_batch = self.parallel_batch
if self.shuffle_and_repeat_fusion is not None:
    pb.shuffle_and_repeat_fusion = self.shuffle_and_repeat_fusion
exit(pb)
