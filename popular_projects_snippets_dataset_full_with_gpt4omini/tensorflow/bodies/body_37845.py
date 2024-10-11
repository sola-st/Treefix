# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
with self.cached_session() as sess:
    reader1 = io_ops.LMDBReader(name="test_read_from_same_file1")
    reader2 = io_ops.LMDBReader(name="test_read_from_same_file2")
    filename_queue = input_lib.string_input_producer(
        [self.db_path], num_epochs=None)
    key1, value1 = reader1.read(filename_queue)
    key2, value2 = reader2.read(filename_queue)

    coord = coordinator.Coordinator()
    threads = queue_runner_impl.start_queue_runners(sess, coord=coord)
    for _ in range(3):
        for _ in range(10):
            k1, v1, k2, v2 = self.evaluate([key1, value1, key2, value2])
            self.assertAllEqual(compat.as_bytes(k1), compat.as_bytes(k2))
            self.assertAllEqual(compat.as_bytes(v1), compat.as_bytes(v2))
    coord.request_stop()
    coord.join(threads)
