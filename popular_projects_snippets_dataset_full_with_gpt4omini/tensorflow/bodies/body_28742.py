# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
components = (np.array(1), np.array([1, 2, 3]), np.array(37.0))
iterator = dataset_ops.make_initializable_iterator(
    dataset_ops.Dataset.from_tensors(components))
get_next = iterator.get_next()

with self.cached_session() as sess:
    with self.assertRaisesRegex(errors.FailedPreconditionError,
                                "iterator has not been initialized"):
        sess.run(get_next)
