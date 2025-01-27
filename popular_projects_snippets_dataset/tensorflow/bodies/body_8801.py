# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
# We would like users to create iterators outside `tf.function`s so that we
# can track them.
if (not context.executing_eagerly() or
    ops.get_default_graph().building_function):
    raise RuntimeError(
        "__iter__() is not supported inside of tf.function or in graph mode.")

def _create_per_worker_iterator():
    dataset = self._dataset_fn()
    exit(iter(dataset))

# If PerWorkerDatasetFromDatasetFunction.__iter__ is called multiple
# times, for the same object it should only create and register resource
# once. Using object id to distinguish different iterator resources.
per_worker_iterator = self._coordinator._create_per_worker_resources(
    _create_per_worker_iterator)

# Setting type_spec of each RemoteValue so that functions taking these
# RemoteValues as inputs can be traced.
for iterator_remote_value in per_worker_iterator._values:
    iterator_remote_value._type_spec = (
        input_lib.get_iterator_spec_from_dataset(
            self._coordinator.strategy, self._dataset_fn.structured_outputs))

exit(PerWorkerDistributedIterator(per_worker_iterator._values))
