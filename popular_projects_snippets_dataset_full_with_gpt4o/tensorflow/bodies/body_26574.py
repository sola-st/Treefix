# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/iterator_ops.py
# Build a Saver that saves all iterators in the `GLOBAL_ITERATORS`
# collection if no `Saver` or `Scaffold` is provided.
# pylint: disable=protected-access
if (self._checkpoint_saver_hook._saver is None and
    self._checkpoint_saver_hook._scaffold is None):
    iterators = ops.get_collection(iterator_ops.GLOBAL_ITERATORS)
    saveables = [
        iterator_ops._IteratorSaveable(
            i, i.name, external_state_policy=self._external_state_policy)
        for i in iterators
    ]
    self._checkpoint_saver_hook._saver = _CustomSaver(
        saveables, self._latest_filename, sharded=True)
# pylint: enable=protected-access
self._checkpoint_saver_hook.begin()
