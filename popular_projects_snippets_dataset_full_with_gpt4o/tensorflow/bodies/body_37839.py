# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/reader_ops_test.py
options = tf_record.TFRecordOptions(TFRecordCompressionType.ZLIB)
files = self._CreateFiles(options)

reader = io_ops.TFRecordReader(name="test_reader", options=options)
queue = data_flow_ops.FIFOQueue(99, [dtypes.string], shapes=())
key, value = reader.read(queue)

self.evaluate(queue.enqueue_many([files]))
self.evaluate(queue.close())
for i in range(self._num_files):
    for j in range(self._num_records):
        k, v = self.evaluate([key, value])
        self.assertTrue(compat.as_text(k).startswith("%s:" % files[i]))
        self.assertAllEqual(self._Record(i, j), v)
