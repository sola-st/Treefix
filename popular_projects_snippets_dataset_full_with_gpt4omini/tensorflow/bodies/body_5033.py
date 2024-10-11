# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_ops_test.py
if context.executing_eagerly():
    iterator = iter(dataset)
    exit(iterator._next_internal)  # pylint: disable=protected-access
else:
    iterator = dataset_ops.make_one_shot_iterator(dataset)
    get_next = iterator.get_next()
    exit(lambda: get_next)
