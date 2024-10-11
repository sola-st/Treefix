# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns an iterator spec from dataset function.

  This function constructs type spec for iterator obtained from
  iter(dataset).

  Args:
    strategy: a `tf.distribute.Strategy` object, used to run all-reduce to
        handle last partial batch.
    dataset: A tf.data.Dataset instance. If using a function that returns a
      tf.data.Dataset instance, pass dataset_fn.structured_outputs.

  Returns:
    A type_spec for iterator for dataset instance.

  """
# pylint: disable=protected-access
output_element_spec = dataset.element_spec
if isinstance(dataset._type_spec,
              (DistributedDatasetSpec,
               DistributedDatasetsFromFunctionSpec)):
    iterator_type_spec = DistributedIteratorSpec(
        strategy.extended._input_workers_with_options(),
        output_element_spec,
        strategy.extended._container_strategy(),
        options=None,
        cardinality=dataset.cardinality,
        enable_get_next_as_optional=True)
else:
    if strategy.extended._num_gpus_per_worker:
        logging.warning(
            f"{strategy.extended._num_gpus_per_worker} GPUs "
            "are allocated per worker. Please use DistributedDataset by "
            "calling strategy.experimental_distribute_dataset or strategy."
            "distribute_datasets_from_function to make best use of GPU "
            "resources"
        )
    iterator_type_spec = iterator_ops.IteratorSpec(output_element_spec)
exit(iterator_type_spec)
