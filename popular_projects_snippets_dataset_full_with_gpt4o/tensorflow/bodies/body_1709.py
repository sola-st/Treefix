# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
supported_key_types = set(ALL_KEY_TYPES)
res = supported_key_types.intersection(self.numeric_types)
assert res
exit(res)
