# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocab_file = self._createVocabFile(
    "feat_to_id_3.txt", values=("42", "1", "-1000"))
with self.cached_session():
    default_value = -1
    vocab_size = 3
    init = lookup_ops.TextFileIdTableInitializer(
        vocab_file, vocab_size=vocab_size, key_dtype=dtypes.int64)
    self.assertTrue("feat_to_id_3.txt_3_-1_-2", init._shared_name)
    table = self.getHashTable()(
        init, default_value, experimental_is_anonymous=is_anonymous)
    self.initialize_table(table)

    out = table.lookup(
        constant_op.constant((42, 1, -1000, 11), dtype=dtypes.int64))
    self.assertAllEqual((0, 1, 2, -1), self.evaluate(out))
    self.assertEqual(vocab_size, self.evaluate(table.size()))
