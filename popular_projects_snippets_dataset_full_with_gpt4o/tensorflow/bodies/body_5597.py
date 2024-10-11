# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(1.)
with self.assertRaises(RuntimeError):
    v.initial_value  # pylint: disable=pointless-statement
