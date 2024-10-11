# Extracted from ./data/repos/black/src/black/trans.py
nonlocal string_child_idx

assert string_parent is not None
assert string_child_idx is not None

string_parent.insert_child(string_child_idx, child)
string_child_idx += 1
