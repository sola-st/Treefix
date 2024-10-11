class Mock: pass # pragma: no cover
ragged_string_ops = type('Mock', (object,), {'ngrams': staticmethod(lambda data, ngram_width, separator, pad_values: [[separator.join([pad_values[0], d[0], d[1]]) for d in group] + [separator.join([d[1], pad_values[1], pad_values[1]]) for d in group] for group in data])})() # pragma: no cover
class Test:  # Simulating behavior of a test class like unittest.TestCase # pragma: no cover
    def evaluate(self, op): return op # pragma: no cover
    def assertAllEqual(self, expected, result): assert expected == result # pragma: no cover
self = Test() # pragma: no cover

class MockRaggedOps: # pragma: no cover
    def ngrams(self, data, ngram_width, separator, pad_values): # pragma: no cover
        result = []# pragma: no cover
        for row in data:# pragma: no cover
            row_result = []# pragma: no cover
            for i in range(len(row) + 2):# pragma: no cover
                left_pad = pad_values[0] if i == 0 else row[i - 1] if i - 1 < len(row) else pad_values[1]# pragma: no cover
                right_pad = pad_values[1] if i == len(row) + 1 else row[i] if i < len(row) else pad_values[1]# pragma: no cover
                row_result.append(separator.join([left_pad, right_pad]))# pragma: no cover
            result.append(row_result)# pragma: no cover
        return result# pragma: no cover
ragged_string_ops = MockRaggedOps() # pragma: no cover
class Test: # pragma: no cover
    def evaluate(self, op): # pragma: no cover
        return op# pragma: no cover
    def assertAllEqual(self, expected, actual): # pragma: no cover
        assert expected == actual, f'Expected {expected}, but got {actual}'# pragma: no cover
self = Test() # pragma: no cover

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
