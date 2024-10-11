# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
with self.assertRaisesRegex(exception, error):
    ragged_string_ops.ngrams(data, ngram_width, separator, pad_values,
                             padding_width, preserve_short_sequences)
