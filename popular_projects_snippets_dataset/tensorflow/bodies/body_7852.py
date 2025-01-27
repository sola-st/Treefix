# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_util.py
"""Returns a distributed dataset from the given input function.

  This is a common function that is used by all strategies to return a
  distributed dataset. The distributed dataset instance returned is different
  depending on if we are in a TF 1 or TF 2 context. The distributed dataset
  instances returned differ from each other in the APIs supported by each of
  them.

  Args:
    dataset_fn: a function that returns a tf.data.Dataset instance.
    input_workers: an InputWorkers object which specifies devices on which
      iterators should be created.
    input_contexts: A list of `InputContext` instances to be passed to call(s)
      to `dataset_fn`. Length and order should match worker order in
      `worker_device_pairs`.
    strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
      handle last partial batch.
    options: Default is None. `tf.distribute.InputOptions` used to control
      options on how this dataset is distributed.
    build: whether to build underlying datasets when a
      `DistributedDatasetFromFunction` is created. This is only useful for
      `ParameterServerStrategy` now.

  Returns:
    A distributed dataset instance.

  Raises:
    ValueError: if `options.experimental_replication_mode` and
    `options.experimental_place_dataset_on_device` are not consistent
  """
if (options is not None and options.experimental_replication_mode !=
    input_lib.InputReplicationMode.PER_REPLICA and
    options.experimental_place_dataset_on_device):
    raise ValueError(
        "When `experimental_place_dataset_on_device` is set for dataset "
        "placement, you must also specify `PER_REPLICA` for the "
        "replication mode")

if (options is not None and options.experimental_replication_mode
    == input_lib.InputReplicationMode.PER_REPLICA and
    options.experimental_fetch_to_device and
    options.experimental_place_dataset_on_device):
    raise ValueError(
        "`experimental_place_dataset_on_device` can not be set to True "
        "when experimental_fetch_to_device is True and "
        "replication mode is set to `PER_REPLICA`")

if tf2.enabled():
    exit(input_lib.DistributedDatasetsFromFunction(
        input_workers,
        strategy,
        input_contexts=input_contexts,
        dataset_fn=dataset_fn,
        options=options,
        build=build,
    ))
else:
    exit(input_lib_v1.DistributedDatasetsFromFunctionV1(
        input_workers, strategy, input_contexts, dataset_fn, options))
