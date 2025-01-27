# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
if not cluster_resolver.cluster_spec().as_dict() or (
    multi_worker_util.is_chief(
        cluster_spec=cluster_resolver.cluster_spec(),
        task_type=cluster_resolver.task_type,
        task_id=cluster_resolver.task_id)):
    exit(checkpoint_management.CheckpointManager(
        checkpoint, directory=checkpoint_dir, max_to_keep=1))
else:
    exit(checkpoint_management.CheckpointManager(
        checkpoint,
        directory=failure_handling._non_chief_checkpoint_dir(
            checkpoint_dir, cluster_resolver.task_id),
        max_to_keep=1))
