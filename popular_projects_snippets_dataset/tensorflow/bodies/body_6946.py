# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
if not (context.executing_eagerly() or
        ops.get_default_graph().building_function):
    raise RuntimeError("__iter__() is only supported inside of tf.function "
                       "or when eager execution is enabled.")
if not self._built:
    raise ValueError("To use this dataset, you need to pass this dataset to "
                     "ClusterCoordinator.create_per_worker_dataset.")

canonicalize_devices = getattr(self._strategy, "_canonicalize_devices",
                               True)

worker_iterators = _create_iterators_per_worker(
    self._cloned_datasets,
    self._input_workers,
    options=self._options,
    canonicalize_devices=canonicalize_devices)
iterator = DistributedIterator(
    self._input_workers,
    worker_iterators,
    self._strategy,
    cardinality=self._cardinality,
    enable_get_next_as_optional=self._enable_get_next_as_optional,
    options=self._options)
iterator._element_spec = self._element_spec  # pylint: disable=protected-access

# When async eager is enabled, sometimes the iterator may not finish
# initialization before passing to a multi device function, add a sync point
# here to make sure all underlying iterators are initialized.
if context.executing_eagerly():
    context.async_wait()

exit(iterator)
