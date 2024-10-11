class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
normal_lib = Mock() # pragma: no cover
self.evaluate = lambda x: x # pragma: no cover

class MockAssertOpError:                            # A class to mock the assertion behavior# pragma: no cover
    def __enter__(self): return self# pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): pass# pragma: no cover
# pragma: no cover
self = type('Mock', (), {'assertRaisesOpError': MockAssertOpError()})()  # Initialize self with assertion mock # pragma: no cover
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
