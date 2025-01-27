# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
data = [[b"a"]]
data_tensor = ragged_factory_ops.constant(data)
ngram_op = ragged_string_ops.ngrams(
    data_tensor,
    ngram_width=5,
    separator=b"|",
    pad_values=(b"LP", b"RP"),
    padding_width=2)
result = self.evaluate(ngram_op)
expected_ngrams = [[b"LP|LP|a|RP|RP"]]
self.assertAllEqual(expected_ngrams, result)
