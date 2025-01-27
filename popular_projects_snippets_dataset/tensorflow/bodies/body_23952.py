# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Verify that writing large contents also works."""

# Make it large (about 5MB)
original = [_TEXT * 10240]
fn = self._WriteRecordsToFile(original, "zlib_read_write_large.tfrecord")
zfn = self._ZlibCompressFile(fn, "zlib_read_write_large.tfrecord.z")

options = tf_record.TFRecordOptions(TFRecordCompressionType.ZLIB)
actual = list(tf_record.tf_record_iterator(zfn, options=options))
self.assertEqual(actual, original)
