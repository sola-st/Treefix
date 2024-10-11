# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
data = [[b"a"], [b"b", b"c", b"d"], [b"e", b"f"]]
data_tensor = ragged_factory_ops.constant(data)
ngram_op = ragged_string_ops.ngrams(
    data_tensor,
    ngram_width=5,
    separator=b"|",
    pad_values=(b"LP", b"RP"),
    padding_width=1,
    preserve_short_sequences=True)
result = self.evaluate(ngram_op)
expected_ngrams = [[b"LP|a|RP"], [b"LP|b|c|d|RP"], [b"LP|e|f|RP"]]
self.assertAllEqual(expected_ngrams, result)
