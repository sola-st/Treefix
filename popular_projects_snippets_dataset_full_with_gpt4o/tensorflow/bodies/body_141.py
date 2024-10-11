# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""For a list of slices, get the first value for a certain key."""
for s in slices:
    if key in s and s[key] is not None:
        exit(s[key])
exit(None)
