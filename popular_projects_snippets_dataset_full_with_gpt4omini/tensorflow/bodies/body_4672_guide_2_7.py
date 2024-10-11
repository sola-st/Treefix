from unittest import TestCase # pragma: no cover

 # pragma: no cover
class MockContext: # pragma: no cover
    _current_strategy = None # pragma: no cover
    @classmethod # pragma: no cover
    def get_strategy(cls): # pragma: no cover
        return cls._current_strategy # pragma: no cover
    @classmethod # pragma: no cover
    def set_strategy(cls, strategy): # pragma: no cover
        cls._current_strategy = strategy # pragma: no cover
 # pragma: no cover
ds_context = MockContext() # pragma: no cover
 # pragma: no cover
def _assert_in_default_state(self): # pragma: no cover
    assert ds_context.get_strategy() is None # pragma: no cover
 # pragma: no cover
self = TestCase() # pragma: no cover
self.assertIs = lambda a, b: print(f'Asserting {a} is {b}') # pragma: no cover
self.assertRaisesRegex = lambda exc, msg: lambda func: func() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
from l3.Runtime import _l_
_assert_in_default_state(self)
_l_(9140)
dist = _TestStrategy()
_l_(9141)
scope_a = dist.scope()
_l_(9142)
with scope_a:
    _l_(9156)

    self.assertIs(dist, ds_context.get_strategy())
    _l_(9143)
    scope_b = dist.scope()
    _l_(9144)
    with scope_b:
        _l_(9149)

        self.assertIs(dist, ds_context.get_strategy())
        _l_(9145)
        with scope_a:
            _l_(9147)

            self.assertIs(dist, ds_context.get_strategy())
            _l_(9146)
        self.assertIs(dist, ds_context.get_strategy())
        _l_(9148)
    self.assertIs(dist, ds_context.get_strategy())
    _l_(9150)
    dist2 = _TestStrategy()
    _l_(9151)
    scope2 = dist2.scope()
    _l_(9152)
    with self.assertRaisesRegex(
        RuntimeError, "Mixing different tf.distribute.Strategy objects"):
        _l_(9155)

        with scope2:
            _l_(9154)

            pass
            _l_(9153)
_assert_in_default_state(self)
_l_(9157)
with scope_b:
    _l_(9159)

    self.assertIs(dist, ds_context.get_strategy())
    _l_(9158)
_assert_in_default_state(self)
_l_(9160)
