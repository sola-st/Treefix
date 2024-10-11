# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Verify that files produced are zlib compatible."""
original = [b"foo", b"bar"]
fn = self._WriteRecordsToFile(original, "zlib_read_write.tfrecord")
zfn = self._ZlibCompressFile(fn, "zlib_read_write.tfrecord.z")

# read the compressed contents and verify.
options = tf_record.TFRecordOptions(TFRecordCompressionType.ZLIB)
actual = list(tf_record.tf_record_iterator(zfn, options=options))
self.assertEqual(actual, original)
