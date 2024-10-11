# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
from l3.Runtime import _l_
_assert_in_default_state(self)
_l_(21578)
dist = _TestStrategy()
_l_(21579)
scope_a = dist.scope()
_l_(21580)
with scope_a:
    _l_(21594)

    self.assertIs(dist, ds_context.get_strategy())
    _l_(21581)
    scope_b = dist.scope()
    _l_(21582)
    with scope_b:
        _l_(21587)

        self.assertIs(dist, ds_context.get_strategy())
        _l_(21583)
        with scope_a:
            _l_(21585)

            self.assertIs(dist, ds_context.get_strategy())
            _l_(21584)
        self.assertIs(dist, ds_context.get_strategy())
        _l_(21586)
    self.assertIs(dist, ds_context.get_strategy())
    _l_(21588)
    dist2 = _TestStrategy()
    _l_(21589)
    scope2 = dist2.scope()
    _l_(21590)
    with self.assertRaisesRegex(
        RuntimeError, "Mixing different tf.distribute.Strategy objects"):
        _l_(21593)

        with scope2:
            _l_(21592)

            pass
            _l_(21591)
_assert_in_default_state(self)
_l_(21595)
with scope_b:
    _l_(21597)

    self.assertIs(dist, ds_context.get_strategy())
    _l_(21596)
_assert_in_default_state(self)
_l_(21598)
