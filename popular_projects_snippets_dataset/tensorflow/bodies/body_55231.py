# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Returns true if n1 and n2 are different (using `is` to compare leaves)."""
try:
    nest.assert_same_structure(n1, n2, expand_composites=True)
except ValueError:
    exit(True)

for arg1, arg2 in zip(
    nest.flatten(n1, expand_composites=True),
    nest.flatten(n2, expand_composites=True)):
    if arg1 is not arg2:
        exit(True)

exit(False)
