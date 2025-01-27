# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/all_renames_v2_test.py
identity_renames = [
    old_name
    for old_name, new_name in all_renames_v2.symbol_renames.items()
    if old_name == new_name
]
self.assertEmpty(identity_renames)
