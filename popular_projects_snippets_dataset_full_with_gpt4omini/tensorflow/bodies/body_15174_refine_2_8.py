class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.evaluate = lambda x: x # pragma: no cover
self.assertAllEqual = lambda x, y: print('Test passed' if x == y else 'Test failed') # pragma: no cover

def mock_ngrams(data, ngram_width, separator, pad_values): # pragma: no cover
    padded_data = [tf.strings.join([pad_values[0]] * (ngram_width - 2) + item + [pad_values[1]] * (ngram_width - 2), separator=separator).numpy().tolist() for item in data] # pragma: no cover
    return [padded_data[i][j:j + ngram_width] for i in range(len(padded_data)) for j in range(len(padded_data[i]) - ngram_width + 1)] # pragma: no cover
class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.evaluate = lambda x: x # pragma: no cover
self.assertAllEqual = lambda x, y: print('Test passed' if x == y else 'Test failed') # pragma: no cover
ragged_string_ops = type('ragged_string_ops', (object,), {'ngrams': mock_ngrams})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/string_ngrams_op_test.py
from l3.Runtime import _l_
data = [[b"a", b"z"], [b"b", b""], [b"e", b"f"]]
_l_(6199)
ngram_op = ragged_string_ops.ngrams(
    data, ngram_width=3, separator=b"|", pad_values=(b"LP", b"RP"))
_l_(6200)
result = self.evaluate(ngram_op)
_l_(6201)
expected_ngrams = [
    [b"LP|LP|a", b"LP|a|z", b"a|z|RP", b"z|RP|RP"],
    [b"LP|LP|b", b"LP|b|", b"b||RP", b"|RP|RP"],
    [b"LP|LP|e", b"LP|e|f", b"e|f|RP", b"f|RP|RP"],
]
_l_(6202)
self.assertAllEqual(expected_ngrams, result)
_l_(6203)
