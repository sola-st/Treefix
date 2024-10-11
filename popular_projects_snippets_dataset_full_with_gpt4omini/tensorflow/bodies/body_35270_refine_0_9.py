class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.evaluate = lambda x: x # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.assertRaisesOpError = staticmethod(lambda msg: lambda func: (lambda: (func(), None))[0] if True else None) # pragma: no cover
self.evaluate = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("Condition x > 0 did not hold"):
    _l_(6518)

    normal = normal_lib.Normal(
        loc=[1.], scale=[-5.], validate_args=True, name="G")
    _l_(6516)
    self.evaluate(normal.mean())
    _l_(6517)
