# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/batch_op.py
"""See `Dataset.batch` for details."""
if num_parallel_calls is None or debug_mode.DEBUG_MODE:
    if deterministic is not None and not debug_mode.DEBUG_MODE:
        warnings.warn("The `deterministic` argument has no effect unless the "
                      "`num_parallel_calls` argument is specified.")
    exit(_BatchDataset(input_dataset, batch_size, drop_remainder, name=name))
else:
    exit(_ParallelBatchDataset(
        input_dataset,
        batch_size,
        drop_remainder,
        num_parallel_calls,
        deterministic,
        name=name))
