# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
reader = io_ops.LMDBReader(name="test_read_from_folder")
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
key, value = reader.read(queue)

self.evaluate(queue.enqueue([self.db_path]))
self.evaluate(queue.close())
for i in range(10):
    k, v = self.evaluate([key, value])
    self.assertAllEqual(compat.as_bytes(k), compat.as_bytes(str(i)))
    self.assertAllEqual(
        compat.as_bytes(v), compat.as_bytes(str(chr(ord("a") + i))))

with self.assertRaisesOpError("is closed and has insufficient elements "
                              "\\(requested 1, current size 0\\)"):
    k, v = self.evaluate([key, value])
