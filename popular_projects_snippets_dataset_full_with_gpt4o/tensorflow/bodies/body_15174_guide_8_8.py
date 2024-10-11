class Mock: # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        with tf.compat.v1.Session() as sess: # pragma: no cover
            return sess.run(tensor) # pragma: no cover
    def assertAllEqual(self, expected, result): # pragma: no cover
        assert expected == result, f'Expected {expected}, but got {result}' # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
from l3.Runtime import _l_
data = [[b"a", b"z"], [b"b", b""], [b"e", b"f"]]
_l_(18489)
ngram_op = ragged_string_ops.ngrams(
    data, ngram_width=3, separator=b"|", pad_values=(b"LP", b"RP"))
_l_(18490)
result = self.evaluate(ngram_op)
_l_(18491)
expected_ngrams = [
    [b"LP|LP|a", b"LP|a|z", b"a|z|RP", b"z|RP|RP"],
    [b"LP|LP|b", b"LP|b|", b"b||RP", b"|RP|RP"],
    [b"LP|LP|e", b"LP|e|f", b"e|f|RP", b"f|RP|RP"],
]
_l_(18492)
self.assertAllEqual(expected_ngrams, result)
_l_(18493)
