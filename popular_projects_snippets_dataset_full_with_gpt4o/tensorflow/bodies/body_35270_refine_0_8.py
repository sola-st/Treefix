from contextlib import contextmanager # pragma: no cover

@contextmanager # pragma: no cover
def assertRaisesOpError(expected_message): # pragma: no cover
    try: # pragma: no cover
        yield # pragma: no cover
    except tf.errors.InvalidArgumentError as e: # pragma: no cover
        assert expected_message in str(e), f'Expected "{expected_message}" to be in "{str(e)}"' # pragma: no cover
    else: # pragma: no cover
        assert False, f'Expected tf.errors.InvalidArgumentError with message "{expected_message}"' # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.assertRaisesOpError = assertRaisesOpError # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("Condition x > 0 did not hold"):
    _l_(18549)

    normal = normal_lib.Normal(
        loc=[1.], scale=[-5.], validate_args=True, name="G")
    _l_(18547)
    self.evaluate(normal.mean())
    _l_(18548)
