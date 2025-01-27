# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
"""Distributes `tf.data.Dataset` instances created by calls to `dataset_fn`.

    `dataset_fn` will be called once for each worker in the strategy. In this
    case, we only have one worker and one device so `dataset_fn` is called
    once.

    The `dataset_fn` should take an `tf.distribute.InputContext` instance where
    information about batching and input replication can be accessed:

    ```
    def dataset_fn(input_context):
      batch_size = input_context.get_per_replica_batch_size(global_batch_size)
      d = tf.data.Dataset.from_tensors([[1.]]).repeat().batch(batch_size)
      return d.shard(
          input_context.num_input_pipelines, input_context.input_pipeline_id)

    inputs = strategy.distribute_datasets_from_function(dataset_fn)

    for batch in inputs:
      replica_results = strategy.run(replica_fn, args=(batch,))
    ```

    IMPORTANT: The `tf.data.Dataset` returned by `dataset_fn` should have a
    per-replica batch size, unlike `experimental_distribute_dataset`, which uses
    the global batch size.  This may be computed using
    `input_context.get_per_replica_batch_size`.

    Args:
      dataset_fn: A function taking a `tf.distribute.InputContext` instance and
        returning a `tf.data.Dataset`.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.

    Returns:
      A "distributed `Dataset`", which the caller can iterate over like regular
      datasets.
    """
exit(super(OneDeviceStrategy,
             self).distribute_datasets_from_function(dataset_fn, options))
