# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py

def g():
    for i in range(10):
        exit(i)

iterator = iterator_ops.Iterator.from_structure(dtypes.int64, [])
next_element = iterator.get_next()

with self.cached_session() as sess:
    dataset_1 = dataset_ops.Dataset.from_generator(
        g, output_types=dtypes.int64)
    sess.run(iterator.make_initializer(dataset_1))
    for expected in range(10):
        self.assertEqual(expected, sess.run(next_element))
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(next_element)

    dataset_2 = dataset_ops.Dataset.from_generator(
        g, output_types=dtypes.int64)
    sess.run(iterator.make_initializer(dataset_2))
    for expected in range(10):
        self.assertEqual(expected, sess.run(next_element))
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(next_element)
