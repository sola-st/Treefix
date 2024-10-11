# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Verify compression with TFRecordWriter is zlib library compatible."""
original = [b"foo", b"bar"]
options = tf_record.TFRecordOptions(TFRecordCompressionType.ZLIB)
fn = self._WriteRecordsToFile(original, "write_zlib_read.tfrecord.z",
                              options)

zfn = self._ZlibDecompressFile(fn, "write_zlib_read.tfrecord")
actual = list(tf_record.tf_record_iterator(zfn))
self.assertEqual(actual, original)
