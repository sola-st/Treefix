# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""test Zlib Compression Type"""
zlib_t = tf_record.TFRecordCompressionType.ZLIB

self.assertEqual(
    "ZLIB",
    tf_record.TFRecordOptions.get_compression_type_string(
        tf_record.TFRecordOptions("ZLIB")))

self.assertEqual(
    "ZLIB",
    tf_record.TFRecordOptions.get_compression_type_string(
        tf_record.TFRecordOptions(zlib_t)))

self.assertEqual(
    "ZLIB",
    tf_record.TFRecordOptions.get_compression_type_string(
        tf_record.TFRecordOptions(tf_record.TFRecordOptions(zlib_t))))
