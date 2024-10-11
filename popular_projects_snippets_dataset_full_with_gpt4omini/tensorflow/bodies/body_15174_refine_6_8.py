class Mock: pass # pragma: no cover
ragged_string_ops = type('Mock', (object,), {'ngrams': staticmethod(lambda data, ngram_width, separator, pad_values: [[separator.join([pad_values[0], d[0], d[1]]) for d in group] + [separator.join([d[1], pad_values[1], pad_values[1]]) for d in group] for group in data])})() # pragma: no cover
class Test:  # Simulating behavior of a test class like unittest.TestCase # pragma: no cover
    def evaluate(self, op): return op # pragma: no cover
    def assertAllEqual(self, expected, result): assert expected == result # pragma: no cover
self = Test() # pragma: no cover

class MockRaggedOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def ngrams(data, ngram_width, separator, pad_values): # pragma: no cover
        result = [] # pragma: no cover
        for row in data: # pragma: no cover
            padded_row = [pad_values[0]] * (ngram_width - 1) + row + [pad_values[1]] * (ngram_width - 1) # pragma: no cover
            ngrams_row = [separator.join(padded_row[i:i + ngram_width]) for i in range(len(padded_row) - ngram_width + 1)] # pragma: no cover
            result.append(ngrams_row) # pragma: no cover
        return result # pragma: no cover
ragged_string_ops = MockRaggedOps() # pragma: no cover
class Mock: # pragma: no cover
    def evaluate(self, op): return op # pragma: no cover
    def assertAllEqual(self, expected, result): assert expected == result, f'Expected {expected}, got {result}' # pragma: no cover
self = Mock() # pragma: no cover

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
