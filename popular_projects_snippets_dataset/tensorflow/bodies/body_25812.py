# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/map_op.py
"""See `Dataset.map()` for details."""
if num_parallel_calls is None or debug_mode.DEBUG_MODE:
    if deterministic is not None and not debug_mode.DEBUG_MODE:
        warnings.warn("The `deterministic` argument has no effect unless the "
                      "`num_parallel_calls` argument is specified.")
    exit(_MapDataset(
        input_dataset, map_func, preserve_cardinality=True, name=name))
else:
    exit(_ParallelMapDataset(
        input_dataset,
        map_func,
        num_parallel_calls=num_parallel_calls,
        deterministic=deterministic,
        preserve_cardinality=True,
        name=name))
