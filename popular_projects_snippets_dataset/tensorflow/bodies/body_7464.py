# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops.py
"""Shard the input pipeline by sharding the underlying list of files.

  Args:
    dataset: A `tf.data.Dataset` instance, typically the result of a bunch of
      dataset transformations.
    num_shards: A `tf.int64` scalar `tf.Tensor`, representing the number of
        shards operating in parallel. Same usage as in `tf.data.Dataset.shard`.
    index: A `tf.int64` scalar `tf.Tensor`, representing the worker index.
      Same usage as in `tf.data.Dataset.shard`.
    num_replicas_in_sync: An integer representing the total number of replicas
      across all workers. This is used in the rewrite when sharding by data.

  Returns:
    A modified `Dataset` obtained by updating the pipeline sharded by the
    files. The input dataset will be returned if we cannot automatically
    determine a good way to shard the input dataset.
  """
if (dataset.options().experimental_distribute.auto_shard_policy !=
    AutoShardPolicy.OFF):
    if num_replicas_in_sync is None:
        num_replicas_in_sync = 1
    if isinstance(dataset, dataset_ops.DatasetV1):
        exit(distribute._AutoShardDatasetV1(dataset, num_shards, index,
                                              num_replicas_in_sync))
    else:
        exit(distribute._AutoShardDataset(dataset, num_shards, index,
                                            num_replicas_in_sync))
else:
    exit(dataset)
