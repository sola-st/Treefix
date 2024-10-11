# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
data = [[b"a"], [b"b", b"c", b"d"], [b"e", b"f"]]
data_tensor = ragged_factory_ops.constant(data)
ngram_op = ragged_string_ops.ngrams(
    data_tensor,
    ngram_width=(1, 5),
    separator=b"|",
    pad_values=(b"LP", b"RP"),
    padding_width=1)
result = self.evaluate(ngram_op)
expected_ngrams = [[b"a"], [b"b", b"c", b"d", b"LP|b|c|d|RP"], [b"e", b"f"]]
self.assertAllEqual(expected_ngrams, result)
