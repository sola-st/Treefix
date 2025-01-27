# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
data = [[[b"a", b"z"], [b"b", b""]], [[b"b", b""], [b"e", b"f"]]]
data_tensor = constant_op.constant(data)
ngram_op = ragged_string_ops.ngrams(
    data_tensor, ngram_width=3, separator=b"|", pad_values=(b"LP", b"RP"))
result = self.evaluate(ngram_op)
expected_ngrams = [[[b"LP|LP|a", b"LP|a|z", b"a|z|RP", b"z|RP|RP"],
                    [b"LP|LP|b", b"LP|b|", b"b||RP", b"|RP|RP"]],
                   [[b"LP|LP|b", b"LP|b|", b"b||RP", b"|RP|RP"],
                    [b"LP|LP|e", b"LP|e|f", b"e|f|RP", b"f|RP|RP"]]]
self.assertIsInstance(ngram_op, ops.Tensor)
self.assertAllEqual(expected_ngrams, result)
