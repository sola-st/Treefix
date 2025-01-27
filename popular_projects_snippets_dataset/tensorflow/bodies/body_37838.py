# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
files = self._CreateFiles()
reader = io_ops.TFRecordReader(name="test_reader")
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
batch_size = 3
key, value = reader.read_up_to(queue, batch_size)

self.evaluate(queue.enqueue_many([files]))
self.evaluate(queue.close())
num_k = 0
num_v = 0

while True:
    try:
        k, v = self.evaluate([key, value])
        # Test reading *up to* batch_size records
        self.assertLessEqual(len(k), batch_size)
        self.assertLessEqual(len(v), batch_size)
        num_k += len(k)
        num_v += len(v)
    except errors_impl.OutOfRangeError:
        break

    # Test that we have read everything
self.assertEqual(self._num_files * self._num_records, num_k)
self.assertEqual(self._num_files * self._num_records, num_v)
