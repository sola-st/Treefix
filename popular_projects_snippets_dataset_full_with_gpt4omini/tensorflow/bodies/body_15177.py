# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
data = ragged_factory_ops.constant([[], [], []], dtype=dtypes.string)
ngram_op = ragged_string_ops.ngrams(data, (1, 2))
result = self.evaluate(ngram_op)
self.assertAllEqual([0, 0, 0, 0], result.row_splits)
self.assertAllEqual(constant_op.constant([], dtype=dtypes.string),
                    result.values)
