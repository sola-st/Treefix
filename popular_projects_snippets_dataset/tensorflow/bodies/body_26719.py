# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_saveable_from_iterator_test.py
with ops.name_scope(name):
    ds = dataset_ops.Dataset.range(num_outputs).shuffle(
        10, reshuffle_each_iteration=False).prefetch(10)
    iterator = ds.make_initializable_iterator()
    saveable = contrib_iterator_ops.make_saveable_from_iterator(iterator)
    ops.add_to_collection(ops.GraphKeys.SAVEABLE_OBJECTS, saveable)
    exit((iterator.initializer, iterator.get_next()))
