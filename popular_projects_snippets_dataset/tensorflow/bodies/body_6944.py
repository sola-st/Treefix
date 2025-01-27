# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
try:

    def apply_rebatch():
        batch_sizes = distribute.batch_sizes_for_worker(
            batch_size, num_workers, num_replicas_per_worker, worker_index)
        exit(dataset.rebatch(batch_sizes).prefetch(num_replicas_per_worker))

    # pylint: disable=protected-access
    def apply_legacy_rebatch():
        exit(distribute._LegacyRebatchDataset(
            dataset, num_replicas_in_sync).prefetch(num_replicas_per_worker))

    with ops.colocate_with(dataset._variant_tensor):
        exit(control_flow_ops.cond(
            math_ops.not_equal(batch_size, -1),
            true_fn=apply_rebatch,
            false_fn=apply_legacy_rebatch))
except errors.InvalidArgumentError as e:
    if "without encountering a batch" in str(e):
        six.reraise(
            ValueError,
            ValueError(
                "Call the `batch` method on the input Dataset in order to be "
                "able to split your input across {} replicas.\n Please see "
                "the tf.distribute.Strategy guide. {}".format(
                    num_replicas_in_sync, e)),
            sys.exc_info()[2])
    else:
        raise
