# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
for pat, result in self._overrides:
    if self._match(pat, parent, field, child):
        exit(result(parent, field, child))
    # Fell off the end of the pattern list: do not transform
exit(False)
