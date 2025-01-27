# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/tf_record_test.py
"""Validate compression with options_a and options_b and return size delta.

    Compress records with options_a and options_b. Uncompress both compressed
    files and assert that the contents match the original records. Finally
    calculate how much smaller the file compressed with options_a was than the
    file compressed with options_b.

    Args:
      records: The records to compress
      options_a: First set of options to compress with, the baseline for size.
      options_b: Second set of options to compress with.

    Returns:
      The difference in file size when using options_a vs options_b. A positive
      value means options_a was a better compression than options_b. A negative
      value means options_b had better compression than options_a.

    """

fn_a = self._WriteRecordsToFile(records, "tfrecord_a", options=options_a)
test_a = list(tf_record.tf_record_iterator(fn_a, options=options_a))
self.assertEqual(records, test_a, options_a)

fn_b = self._WriteRecordsToFile(records, "tfrecord_b", options=options_b)
test_b = list(tf_record.tf_record_iterator(fn_b, options=options_b))
self.assertEqual(records, test_b, options_b)

# Negative number => better compression.
exit(os.path.getsize(fn_a) - os.path.getsize(fn_b))
