# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
reader = io_ops.WholeFileReader("test_reader")
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
self.evaluate(queue.enqueue_many([self._filenames]))
self.evaluate(queue.close())
key, value = reader.read(queue)

self._ExpectRead(key, value, 0)
self._ExpectRead(key, value, 1)
self._ExpectRead(key, value, 2)

with self.assertRaisesOpError("is closed and has insufficient elements "
                              "\\(requested 1, current size 0\\)"):
    self.evaluate([key, value])
