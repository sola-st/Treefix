# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
reader = io_ops.IdentityReader("test_reader")
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
enqueue = queue.enqueue_many([["DD", "EE"]])
key, value = reader.read(queue)

self.evaluate(enqueue)
self._ExpectRead(key, value, b"DD")
self._ExpectRead(key, value, b"EE")
self.evaluate(enqueue)
self._ExpectRead(key, value, b"DD")
self._ExpectRead(key, value, b"EE")
self.evaluate(enqueue)
self._ExpectRead(key, value, b"DD")
self._ExpectRead(key, value, b"EE")
self.evaluate(queue.close())
with self.assertRaisesOpError("is closed and has insufficient elements "
                              "\\(requested 1, current size 0\\)"):
    self.evaluate([key, value])
