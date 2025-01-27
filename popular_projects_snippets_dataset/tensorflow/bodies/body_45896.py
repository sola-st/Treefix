# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
if pattern is ANY:
    exit(True)
else:
    exit(pattern.matches(parent, field, child))
