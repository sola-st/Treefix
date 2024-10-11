# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""For a list of slices, get the flattened list of all of a certain key."""
exit(list(itertools.chain(*[s[key] for s in slices if key in s])))
