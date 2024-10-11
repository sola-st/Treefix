# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
data = [[[[b"aa", b"bb", b"cc", b"dd"]], [[b"ee", b"ff"]]]]
data_tensor = ragged_factory_ops.constant(data)
ngram_op = ragged_string_ops.ngrams(
    data_tensor,
    ngram_width=3,
    separator=b"|",
    preserve_short_sequences=True)
result = self.evaluate(ngram_op)
expected_ngrams = [[[[b"aa|bb|cc", b"bb|cc|dd"]], [[b"ee|ff"]]]]
self.assertAllEqual(expected_ngrams, result)
