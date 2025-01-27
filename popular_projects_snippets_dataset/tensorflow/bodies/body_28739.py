# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
# Define a dataset whose initialization will always fail.
dataset = dataset_ops.Dataset.from_tensors(array_ops.gather([0], [4]))
iterator = dataset_ops.make_one_shot_iterator(dataset)
next_element = iterator.get_next()

with self.cached_session() as sess:
    with self.assertRaisesRegex(errors.InvalidArgumentError, ""):
        sess.run(next_element)

    # Test that subsequent attempts to use the iterator also fail.
    with self.assertRaisesRegex(errors.InvalidArgumentError, ""):
        sess.run(next_element)

with self.cached_session() as sess:

    def consumer_thread():
        with self.assertRaisesRegex(errors.InvalidArgumentError, ""):
            sess.run(next_element)

    num_threads = 8
    threads = [
        self.checkedThread(consumer_thread) for _ in range(num_threads)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
