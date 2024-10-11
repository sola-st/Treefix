# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
oov_buckets = 5

# Set a table that only uses hash buckets, for each input value returns
# an id calculated by fingerprint("input") mod oov_buckets.
table = self.getVocabularyTable()(
    None, oov_buckets, experimental_is_anonymous=is_anonymous)
self.initialize_table(table)

values = constant_op.constant(("brain", "salad", "surgery"))

out = table.lookup(values)
self.assertAllEqual(
    [
        3,  # fingerprint("brain") mod 5.
        1,  # fingerprint("salad") mod 5.
        4  # fingerprint("surgery") mod 5
    ],
    self.evaluate(out))
self.assertEqual(oov_buckets, self.evaluate(table.size()))
