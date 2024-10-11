# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
super(TFRecordWriterCloseAndFlushTests, self).setUp()
self._fn = os.path.join(self.get_temp_dir(), "tf_record_writer_test.txt")
self._options = tf_record.TFRecordOptions(compression_type)
self._writer = tf_record.TFRecordWriter(self._fn, self._options)
self._num_records = 20
