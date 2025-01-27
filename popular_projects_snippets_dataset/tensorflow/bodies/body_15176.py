# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
data = [[b"a", b"b", b"c", b"d"], [b"e", b"f", b"g", b"h"]]
data_tensor = ragged_factory_ops.constant(data)
ngram_op = ragged_string_ops.ngrams(
    data_tensor, ngram_width=(1, 2, 3), separator=b"|")
result = self.evaluate(ngram_op)
expected_ngrams = [[
    b"a", b"b", b"c", b"d", b"a|b", b"b|c", b"c|d", b"a|b|c", b"b|c|d"
], [b"e", b"f", b"g", b"h", b"e|f", b"f|g", b"g|h", b"e|f|g", b"f|g|h"]]
self.assertAllEqual(expected_ngrams, result)
