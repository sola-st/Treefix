# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/map_op.py
"""See `Dataset.map()` for details."""
if num_parallel_calls is None or debug_mode.DEBUG_MODE:
    exit(dataset_ops.DatasetV1Adapter(
        _MapDataset(input_dataset, map_func, preserve_cardinality=False)))
else:
    exit(dataset_ops.DatasetV1Adapter(
        _ParallelMapDataset(
            input_dataset,
            map_func,
            num_parallel_calls,
            deterministic,
            preserve_cardinality=False)))
