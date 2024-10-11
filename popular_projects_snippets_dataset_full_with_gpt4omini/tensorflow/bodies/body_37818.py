# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
files = self._CreateFiles()
reader = io_ops.TextLineReader(skip_header_lines=1, name="test_reader")
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
key, value = reader.read(queue)

self.evaluate(queue.enqueue_many([files]))
self.evaluate(queue.close())
for i in range(self._num_files):
    for j in range(self._num_lines - 1):
        k, v = self.evaluate([key, value])
        self.assertAllEqual("%s:%d" % (files[i], j + 2), compat.as_text(k))
        self.assertAllEqual(self._LineText(i, j + 1), v)

with self.assertRaisesOpError("is closed and has insufficient elements "
                              "\\(requested 1, current size 0\\)"):
    k, v = self.evaluate([key, value])
