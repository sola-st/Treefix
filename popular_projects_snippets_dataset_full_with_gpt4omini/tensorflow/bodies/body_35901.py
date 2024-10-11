# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
vs = variable_scope._get_default_variable_store()
# No check by default, so we can both create and get existing names.
v = vs.get_variable("v", [1])
v1 = vs.get_variable("v", [1])
self.assertIs(v, v1)

# When reuse is False, we fail when variables are already there.
vs.get_variable("w", [1], reuse=False)  # That's ok.
with self.assertRaises(ValueError):
    vs.get_variable("v", [1], reuse=False)  # That fails.
# When reuse is True, we fail when variables are new.
vs.get_variable("v", [1], reuse=True)  # That's ok.
with self.assertRaises(ValueError):
    vs.get_variable("u", [1], reuse=True)  # That fails.
