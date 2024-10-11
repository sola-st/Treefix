# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_test.py
if ((not n) and
    ((target in (unconditional_return_in_single_while,
                 effectively_unconditional_return_in_single_while)))):
    self.skipTest('Undefined symbols require at least one iteration.')

n = type_(n)
self.assertFunctionMatchesEager(target, n)
