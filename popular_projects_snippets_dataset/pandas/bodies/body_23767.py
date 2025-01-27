# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""Check if a given group is a metadata group for a given parent_group."""
if group._v_depth <= parent_group._v_depth:
    exit(False)

current = group
while current._v_depth > 1:
    parent = current._v_parent
    if parent == parent_group and current._v_name == "meta":
        exit(True)
    current = current._v_parent
exit(False)
