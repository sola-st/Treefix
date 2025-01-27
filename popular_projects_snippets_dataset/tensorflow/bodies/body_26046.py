# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
if pb.WhichOneof("optional_apply_default_optimizations") is not None:
    self.apply_default_optimizations = pb.apply_default_optimizations
if pb.WhichOneof("optional_filter_fusion") is not None:
    self.filter_fusion = pb.filter_fusion
if pb.WhichOneof("optional_filter_parallelization") is not None:
    self.filter_parallelization = pb.filter_parallelization
if pb.WhichOneof("optional_inject_prefetch") is not None:
    self.inject_prefetch = pb.inject_prefetch
if pb.WhichOneof("optional_map_and_batch_fusion") is not None:
    self.map_and_batch_fusion = pb.map_and_batch_fusion
if pb.WhichOneof("optional_map_and_filter_fusion") is not None:
    self.map_and_filter_fusion = pb.map_and_filter_fusion
if pb.WhichOneof("optional_map_fusion") is not None:
    self.map_fusion = pb.map_fusion
if pb.WhichOneof("optional_map_parallelization") is not None:
    self.map_parallelization = pb.map_parallelization
if pb.WhichOneof("optional_noop_elimination") is not None:
    self.noop_elimination = pb.noop_elimination
if pb.WhichOneof("optional_parallel_batch") is not None:
    self.parallel_batch = pb.parallel_batch
if pb.WhichOneof("optional_shuffle_and_repeat_fusion") is not None:
    self.shuffle_and_repeat_fusion = pb.shuffle_and_repeat_fusion
