# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
vocab_file = self._createVocabFile("feat_to_id_7.txt")
input_row_splits = [0, 2, 4, 5]
ragged_features = ragged_tensor.RaggedTensor.from_row_splits(
    constant_op.constant(["brain", "salad", "brain", "surgery", "tarkus"],
                         dtypes.string),
    constant_op.constant(input_row_splits, dtypes.int64))

table = self.getVocabularyTable()(
    lookup_ops.TextFileIdTableInitializer(vocab_file, vocab_size=3),
    1,
    experimental_is_anonymous=is_anonymous)
self.initialize_table(table)

ragged_ids = table.lookup(ragged_features)

self.assertAllEqual([5], ragged_ids.values._shape_as_list())

ragged_ids_val, ragged_ids_row_splits = self.evaluate(
    [ragged_ids.values, ragged_ids.row_splits])

self.assertAllEqual([0, 1, 0, 2, 3], ragged_ids_val)
self.assertAllEqual(input_row_splits, ragged_ids_row_splits)
