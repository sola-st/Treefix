# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/save_op.py
"""Implements the save function and checkpoint functionality."""
if context.executing_eagerly() and checkpoint_args:
    save_dataset = _SaveDataset(input_dataset, path, shard_func, compression)
    save_iterator = iter(save_dataset)

    if "checkpoint" in checkpoint_args:
        raise ValueError(
            "'Invalid `checkpoint_args`. `checkpoint_args` are not allowed "
            "to include 'checkpoint'."
        )
    checkpoint = checkpoint_lib.Checkpoint(iterator=save_iterator)
    checkpoint_args["checkpoint"] = checkpoint
    manager = checkpoint_management.CheckpointManager(**checkpoint_args)
    checkpoint.restore(manager.latest_checkpoint)

    for _ in enumerate(save_iterator):
        if "step_counter" in checkpoint_args:
            checkpoint_args["step_counter"].assign_add(delta=1)
        manager.save(check_interval=True)
else:
    dataset, shard_func, use_shard_func, path = set_save_dataset_attributes(
        input_dataset, shard_func, path)
    ged_ops.save_dataset(
        dataset._variant_tensor,   # pylint: disable=protected-access
        path=path,
        shard_func_other_args=shard_func.captured_inputs,
        compression=compression,
        shard_func=shard_func,
        use_shard_func=use_shard_func)
