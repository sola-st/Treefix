# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
dataset = dataset_ops.Dataset.from_tensors([1, 2, 3]).map(lambda x: x * x)
iterator = dataset_ops.make_one_shot_iterator(dataset)
next_element = iterator.get_next()

# Create a session with a single thread to ensure that the
# one-shot iterator initializer does not deadlock.
config = config_pb2.ConfigProto(
    inter_op_parallelism_threads=1, use_per_session_threads=True)
with session.Session(config=config) as sess:
    self.assertAllEqual([1, 4, 9], sess.run(next_element))
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(next_element)

    # Test with multiple threads invoking the one-shot iterator concurrently.
with session.Session(config=config) as sess:
    results = []

    def consumer_thread():
        try:
            results.append(sess.run(next_element))
        except errors.OutOfRangeError:
            results.append(None)

    num_threads = 8
    threads = [
        self.checkedThread(consumer_thread) for _ in range(num_threads)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    self.assertLen(results, num_threads)
    self.assertLen([None for r in results if r is None], num_threads - 1)
    self.assertAllEqual([[1, 4, 9]], [r for r in results if r is not None])
