# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
reader = io_ops.FixedLengthRecordReader(
    header_bytes=self._header_bytes,
    record_bytes=self._record_bytes,
    footer_bytes=self._footer_bytes,
    hop_bytes=self._hop_bytes,
    encoding=encoding,
    name="test_reader")
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
key, value = reader.read(queue)

self.evaluate(queue.enqueue_many([files]))
self.evaluate(queue.close())
for i in range(self._num_files):
    for j in range(num_overlapped_records):
        k, v = self.evaluate([key, value])
        self.assertAllEqual("%s:%d" % (files[i], j), compat.as_text(k))
        self.assertAllEqual(self._OverlappedRecord(i, j), v)

with self.assertRaisesOpError("is closed and has insufficient elements "
                              "\\(requested 1, current size 0\\)"):
    k, v = self.evaluate([key, value])
