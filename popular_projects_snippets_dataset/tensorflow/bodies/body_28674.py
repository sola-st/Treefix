# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
dataset = dataset_ops.Dataset.from_tensors((42, None))
if context.executing_eagerly():
    self.assertDatasetProduces(dataset, expected_output=[(42, None)])
else:
    iterator = dataset_ops.make_one_shot_iterator(dataset)
    next_first, next_second = iterator.get_next()
    self.assertIsNone(next_second)
    with self.cached_session() as sess:
        self.assertEqual(sess.run(next_first), 42)
