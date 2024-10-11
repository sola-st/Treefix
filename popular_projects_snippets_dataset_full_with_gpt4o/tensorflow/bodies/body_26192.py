# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
exit(DatasetV1Adapter(
    super(DatasetV1, self).interleave(
        map_func,
        cycle_length,
        block_length,
        num_parallel_calls,
        deterministic,
        name=name)))
