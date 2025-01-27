# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/file_system_test.py
with self.cached_session() as sess:
    reader = io_ops.WholeFileReader("test_reader")
    queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
    queue.enqueue_many([["test://foo"]]).run()
    queue.close().run()
    key, value = self.evaluate(reader.read(queue))
self.assertEqual(key, compat.as_bytes("test://foo"))
self.assertEqual(value, compat.as_bytes("AAAAAAAAAA"))
