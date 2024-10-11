# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""test No Compression Type"""
self.assertEqual(
    "",
    tf_record.TFRecordOptions.get_compression_type_string(
        tf_record.TFRecordOptions()))

self.assertEqual(
    "",
    tf_record.TFRecordOptions.get_compression_type_string(
        tf_record.TFRecordOptions("")))

with self.assertRaises(ValueError):
    tf_record.TFRecordOptions(5)

with self.assertRaises(ValueError):
    tf_record.TFRecordOptions("BZ2")
