# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Distribute the dataset on all workers.

    If `num_replicas_in_sync` is not None, we split each batch of the dataset
    into `num_replicas_in_sync` smaller batches, to be distributed among that
    worker's replicas, so that the batch size for a global step (across all
    workers and replicas) is as expected.

    Args:
      input_workers: an `InputWorkers` object.
      strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
        handle last partial batch.
      dataset: `tf.data.Dataset` that will be used as the input source. Either
        dataset or components field should be passed when constructing
        DistributedDataset. Use this when contructing DistributedDataset from a
        new `tf.data.Dataset`. Use components when constructing using
        DistributedDatasetSpec.
      num_replicas_in_sync: Optional integer. If this is not None, the value
        is used to decide how to rebatch datasets into smaller batches so that
        the total batch size for each step (across all workers and replicas)
        adds up to `dataset`'s batch size.
      input_context: `InputContext` for sharding. Only pass this in for between
        graph multi-worker cases where there is only one `input_worker`. In
        these cases, we will shard based on the `input_pipeline_id` and
        `num_input_pipelines` in the `InputContext`.
      components: datasets when DistributedDataset is constructed from
        DistributedDatasetSpec. Either field dataset or components should be
        passed.
      element_spec: element spec for DistributedDataset when constructing from
        DistributedDatasetSpec. This will be used to set the element_spec for
        DistributedDataset and verified against element_spec from components.
      enable_get_next_as_optional: this is required when components is passed
        instead of dataset.
      build: whether to build underlying datasets when this object is created.
        This is only useful for `ParameterServerStrategy` now.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.
    """
super(DistributedDataset, self).__init__(input_workers=input_workers)
if input_workers is None or strategy is None:
    raise ValueError("input_workers and strategy are required arguments")
if dataset is not None and components is not None:
    raise ValueError("Only one of dataset or components should be present")
if dataset is None and components is None:
    raise ValueError("At least one of dataset or components should be passed")

self._input_workers = input_workers
self._strategy = strategy
self._options = options
self._input_context = input_context
self._num_replicas_in_sync = num_replicas_in_sync

if dataset is not None:
    self._original_dataset = dataset
    self._built = False
    if build:
        self.build()
else:
    if not build:
        raise ValueError(
            "When constructing DistributedDataset with components, build "
            "should not be False. This is an internal error. Please file a "
            "bug.")
    if enable_get_next_as_optional is None:
        raise ValueError(
            "When constructing DistributedDataset with components, " +
            "enable_get_next_as_optional should also be passed")
    self._cloned_datasets = components
    self._cardinality = _cardinality(self._cloned_datasets[0])
    self._enable_get_next_as_optional = enable_get_next_as_optional

    assert element_spec is not None
    if element_spec != _create_distributed_tensor_spec(
        self._strategy, self._cloned_datasets[0].element_spec):
        raise ValueError("Mismatched element_spec from the passed components")
    self._element_spec = element_spec

    self._built = True
