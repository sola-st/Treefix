# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
data = [b"a", b"z"]
data_tensor = ragged_factory_ops.constant(data)
ngram_op = ragged_string_ops.ngrams(
    data_tensor, ngram_width=3, separator=b"|", pad_values=(b"LP", b"RP"))
result = self.evaluate(ngram_op)
expected_ngrams = [b"LP|LP|a", b"LP|a|z", b"a|z|RP", b"z|RP|RP"]
self.assertAllEqual(expected_ngrams, result)
