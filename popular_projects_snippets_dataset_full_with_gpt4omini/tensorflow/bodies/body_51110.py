# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
"""Enforces names are uppercase versions of values."""
for policy in save_options.VariablePolicy:
    if policy == save_options.VariablePolicy.NONE:
        self.assertIsNone(policy.value)
    else:
        self.assertEqual(policy.name, policy.name.upper())
        self.assertEqual(policy.value, policy.value.lower())
        self.assertEqual(policy.name, policy.value.upper())
