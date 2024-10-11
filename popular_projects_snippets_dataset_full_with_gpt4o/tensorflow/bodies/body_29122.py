# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
ph1 = array_ops.placeholder(dtypes.int32, shape=[None])
ph2 = array_ops.placeholder(dtypes.int32, shape=None)
data = dataset_ops.Dataset.from_tensors((ph1, ph2))
data = data.unbatch()
iterator = dataset_ops.make_initializable_iterator(data)
next_element = iterator.get_next()

with self.cached_session() as sess:
    # Mismatch in the 0th dimension.
    sess.run(
        iterator.initializer,
        feed_dict={
            ph1: np.arange(7).astype(np.int32),
            ph2: np.arange(8).astype(np.int32)
        })
    with self.assertRaises(errors.InvalidArgumentError):
        self.evaluate(next_element)

    # No 0th dimension (i.e. scalar value) for one component.
    sess.run(
        iterator.initializer,
        feed_dict={
            ph1: np.arange(7).astype(np.int32),
            ph2: 7
        })
    with self.assertRaises(errors.InvalidArgumentError):
        self.evaluate(next_element)
