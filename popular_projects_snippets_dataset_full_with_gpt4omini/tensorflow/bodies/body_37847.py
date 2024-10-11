# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
with self.cached_session() as sess:
    reader = io_ops.LMDBReader(name="test_read_from_file_repeated")
    filename_queue = input_lib.string_input_producer(
        [self.db_path], num_epochs=None)
    key, value = reader.read(filename_queue)

    coord = coordinator.Coordinator()
    threads = queue_runner_impl.start_queue_runners(sess, coord=coord)
    # Iterate over the lmdb 3 times.
    for _ in range(3):
        # Go over all 10 records each time.
        for j in range(10):
            k, v = self.evaluate([key, value])
            self.assertAllEqual(compat.as_bytes(k), compat.as_bytes(str(j)))
            self.assertAllEqual(
                compat.as_bytes(v), compat.as_bytes(str(chr(ord("a") + j))))
    coord.request_stop()
    coord.join(threads)
