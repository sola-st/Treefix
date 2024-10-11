from unittest.mock import Mock # pragma: no cover

_assert_in_default_state = Mock() # pragma: no cover
self = Mock() # pragma: no cover
ds_context = Mock() # pragma: no cover
self.assertIs = Mock() # pragma: no cover
self.assertRaisesRegex = Mock() # pragma: no cover

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
