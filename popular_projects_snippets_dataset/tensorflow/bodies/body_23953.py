# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Verify that files produced are gzip compatible."""
original = [b"foo", b"bar"]
fn = self._WriteRecordsToFile(original, "gzip_read_write.tfrecord")
gzfn = self._GzipCompressFile(fn, "tfrecord.gz")

options = tf_record.TFRecordOptions(TFRecordCompressionType.GZIP)
actual = list(tf_record.tf_record_iterator(gzfn, options=options))
self.assertEqual(actual, original)
