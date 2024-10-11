# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocab_file = self._createVocabFile("vocab.txt")
vocab_size = 3
oov_buckets = 1
table = self.getVocabularyTable()(
    lookup_ops.TextFileIdTableInitializer(
        vocab_file, vocab_size=vocab_size),
    oov_buckets,
    experimental_is_anonymous=is_anonymous)
objects = checkpoint_util.list_objects(graph_view.ObjectGraphView(table))
assets = list(filter(lambda obj: isinstance(obj, asset.Asset), objects))
self.assertLen(assets, 1)
self.assertEqual(
    self.evaluate(assets[0].asset_path), compat.as_bytes(vocab_file))
