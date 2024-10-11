# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Verify compression for large records is zlib library compatible."""
# Make it large (about 5MB)
original = [_TEXT * 10240]
options = tf_record.TFRecordOptions(TFRecordCompressionType.ZLIB)
fn = self._WriteRecordsToFile(original, "write_zlib_read_large.tfrecord.z",
                              options)
zfn = self._ZlibDecompressFile(fn, "write_zlib_read_large.tfrecord")
actual = list(tf_record.tf_record_iterator(zfn))
self.assertEqual(actual, original)
