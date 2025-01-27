# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
"""Test for same behavior when the seed is a Python or Tensor zero."""
iterator = dataset_ops.make_one_shot_iterator(
    dataset_ops.Dataset.range(10).shuffle(10, seed=0))
get_next = iterator.get_next()

elems = []
with self.cached_session() as sess:
    for _ in range(10):
        elems.append(sess.run(get_next))
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(get_next)

seed_placeholder = array_ops.placeholder(dtypes.int64, shape=[])
iterator = dataset_ops.make_initializable_iterator(
    dataset_ops.Dataset.range(10).shuffle(10, seed=seed_placeholder))
get_next = iterator.get_next()

with self.cached_session() as sess:
    sess.run(iterator.initializer, feed_dict={seed_placeholder: 0})
    for elem in elems:
        self.assertEqual(elem, sess.run(get_next))
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(get_next)
