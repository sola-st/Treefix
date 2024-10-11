# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_test.py
if ((type_ is _int_dataset) and
    (target in (unconditional_return_in_single_for,
                effectively_unconditional_return_in_single_for))):
    # TODO(mdan): Enable in a separate improvement.
    self.skipTest('Creating symbols in dataset loops.')

if ((not l) and
    ((target in (unconditional_return_in_single_for,
                 effectively_unconditional_return_in_single_for)))):
    self.skipTest('Undefined symbols require at least one iteration.')

l = type_(l)
self.assertFunctionMatchesEager(target, l)
