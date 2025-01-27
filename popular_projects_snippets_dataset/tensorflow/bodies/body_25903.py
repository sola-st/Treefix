# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/interleave_op.py
"""See `Dataset.interleave()` for details."""
if block_length is None:
    block_length = 1

if cycle_length is None:
    cycle_length = dataset_ops.AUTOTUNE

if num_parallel_calls is None or debug_mode.DEBUG_MODE:
    if deterministic is not None and not debug_mode.DEBUG_MODE:
        warnings.warn("The `deterministic` argument has no effect unless the "
                      "`num_parallel_calls` argument is specified.")
    exit(_InterleaveDataset(
        input_dataset, map_func, cycle_length, block_length, name=name))
else:
    exit(_ParallelInterleaveDataset(
        input_dataset,
        map_func,
        cycle_length,
        block_length,
        num_parallel_calls,
        deterministic=deterministic,
        name=name))
