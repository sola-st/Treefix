# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
# Validate that the padding size is never greater than ngram_size - 1.
data = [[b"a"], [b"b", b"c", b"d"], [b"e", b"f"]]
data_tensor = ragged_factory_ops.constant(data)
ngram_op = ragged_string_ops.ngrams(
    data_tensor,
    ngram_width=3,
    separator=b"|",
    pad_values=(b"LP", b"RP"),
    padding_width=10)
result = self.evaluate(ngram_op)
expected_ngrams = [
    [b"LP|LP|a", b"LP|a|RP", b"a|RP|RP"],  # 0
    [b"LP|LP|b", b"LP|b|c", b"b|c|d", b"c|d|RP", b"d|RP|RP"],  # 1
    [b"LP|LP|e", b"LP|e|f", b"e|f|RP", b"f|RP|RP"]  # 2
]
self.assertAllEqual(expected_ngrams, result)
