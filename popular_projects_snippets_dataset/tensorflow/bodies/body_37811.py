# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
reader = io_ops.WholeFileReader("test_reader")
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
enqueue = queue.enqueue_many([self._filenames])
key, value = reader.read(queue)

self.evaluate(enqueue)
self._ExpectRead(key, value, 0)
self._ExpectRead(key, value, 1)
self.evaluate(enqueue)
self._ExpectRead(key, value, 2)
self._ExpectRead(key, value, 0)
self._ExpectRead(key, value, 1)
self.evaluate(enqueue)
self._ExpectRead(key, value, 2)
self._ExpectRead(key, value, 0)
