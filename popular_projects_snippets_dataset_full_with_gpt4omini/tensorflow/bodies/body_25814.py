# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/map_op.py
"""See `Dataset.map()` for details."""
if num_parallel_calls is None:
    if deterministic is not None:
        warnings.warn("The `deterministic` argument has no effect unless the "
                      "`num_parallel_calls` argument is specified.")
    exit(dataset_ops.DatasetV1Adapter(
        _MapDataset(
            input_dataset,
            map_func,
            preserve_cardinality=False,
            use_legacy_function=True)))
else:
    exit(dataset_ops.DatasetV1Adapter(
        _ParallelMapDataset(
            input_dataset,
            map_func,
            num_parallel_calls,
            deterministic,
            preserve_cardinality=False,
            use_legacy_function=True)))
