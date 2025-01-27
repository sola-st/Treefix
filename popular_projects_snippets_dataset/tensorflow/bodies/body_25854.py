# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/snapshot_op.py
"""See `Dataset.snapshot()` for details."""

project_func = None
if shard_func is None:
    input_dataset = input_dataset.enumerate(name=name)
    # This sets the amount of parallelism based on the number of CPU cores on
    # the machine where this Python code is executed, which may differ from
    # the number of CPU cores where the input pipeline graph is actually
    # executed (e.g. remote Cloud TPU workers).
    local_shard_func = lambda index, _: index % multiprocessing.cpu_count()
    project_func = lambda _, elem: elem
else:
    local_shard_func = shard_func
dataset = _SnapshotDataset(
    input_dataset=input_dataset,
    path=path,
    compression=compression,
    reader_func=reader_func,
    # This will not do the right thing where the graph is built on a
    # different machine than the executor (e.g. Cloud TPUs).
    shard_func=local_shard_func,
    name=name)
if project_func is not None:
    dataset = dataset.map(project_func, name=name)
exit(dataset)
