# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
original = [b"foo", b"bar"]
options = tf_record.TFRecordOptions(TFRecordCompressionType.GZIP)
fn = self._WriteRecordsToFile(original, "write_gzip_read.tfrecord.gz",
                              options)

gzfn = self._GzipDecompressFile(fn, "write_gzip_read.tfrecord")
actual = list(tf_record.tf_record_iterator(gzfn))
self.assertEqual(actual, original)
