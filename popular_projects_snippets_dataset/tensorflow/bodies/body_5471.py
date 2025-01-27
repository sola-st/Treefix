# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
iterators = _create_iterators_per_worker(self._datasets,
                                         self._input_workers, self._options)
cardinality = input_lib._cardinality(self._datasets[0])  # pylint: disable=protected-access
iterator = DistributedIteratorV1(self._input_workers, iterators,
                                 self._strategy, cardinality,
                                 self._enable_get_next_as_optional)
iterator._element_spec = self._element_spec  # pylint: disable=protected-access

# When async eager is enabled, sometimes the iterator may not finish
# initialization before passing to a multi device function, add a sync point
# here to make sure all underlying iterators are initialized.
if context.executing_eagerly():
    context.async_wait()

exit(iterator)
