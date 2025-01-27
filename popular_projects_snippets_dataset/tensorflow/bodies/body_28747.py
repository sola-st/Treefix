# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
dataset = dataset_ops.Dataset.range(0)
iterator = iterator_ops.Iterator.from_structure(
    dataset_ops.get_legacy_output_types(dataset), [])
init_op = iterator.make_initializer(dataset)

with self.cached_session() as sess:
    sess.run(init_op)
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(iterator.get_next())
