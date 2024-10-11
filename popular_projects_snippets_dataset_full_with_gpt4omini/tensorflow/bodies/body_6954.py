# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Makes an iterable from datasets created by the given function.

    Args:
      input_workers: an `InputWorkers` object.
      strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
        handle last partial batch.
      input_contexts: A list of `InputContext` instances to be passed to call(s)
        to `dataset_fn`. Length and order should match worker order in
        `worker_device_pairs`.
      dataset_fn: A function that returns a `Dataset` given an `InputContext`.
        Either dataset_fn or components should be passed to construct
        DistributedDatasetsFromFunction. Use this when constructing
        DistributedDataset using a function. Use components when constructing
        using DistributedDatasetsFromFunctionSpec.
      options: `tf.distribute.InputOptions` used to control options on how this
        dataset is distributed.
      components: datasets when DistributedDatasetsFromFunction is constructed
        from DistributedDatasetsFromFunctionSpec. Only one of dataset or
        components should be passed.
      element_spec: element spec for DistributedDataset when constructing from
        DistributedDatasetSpec. This will be used to set the element_spec for
        DistributedDatasetsFromFunctionSpec and verified against element_spec
        from components.
      build: whether to build underlying datasets when this object is created.
        This is only useful for `ParameterServerStrategy` now.
    """
super(DistributedDatasetsFromFunction, self).__init__(
    input_workers=input_workers)
self._input_workers = input_workers
self._strategy = strategy
self._options = options
if dataset_fn is not None and components is not None:
    raise ValueError("Only one of dataset_fn or components should be set")
if dataset_fn is None and components is None:
    raise ValueError("At least one of dataset_fn or components should be set")

if dataset_fn is not None:
    if input_workers.num_workers != len(input_contexts):
        raise ValueError(
            "Number of input workers (%d) is not same as number of "
            "input_contexts (%d)" %
            (input_workers.num_workers, len(input_contexts)))
    self._input_contexts = input_contexts
    self._dataset_fn = dataset_fn
    self._built = False
    if build:
        self.build()
else:
    if element_spec is None:
        raise ValueError(
            "element_spec should also be passed when passing components")
    if not build:
        raise ValueError(
            "When constructing DistributedDatasetFromFunction with components, "
            "build should not be False. This is an internal error. Please file "
            "a bug.")
    self._element_spec = element_spec
    self._datasets = components
    self._built = True
    self._cardinality = _cardinality(self._datasets[0])
    self._enable_get_next_as_optional = _enable_get_next_as_optional(
        self._strategy, self._datasets[0], self._cardinality)
