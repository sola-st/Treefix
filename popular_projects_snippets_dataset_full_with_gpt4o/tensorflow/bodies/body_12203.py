# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2_indexed_slices_rewriter.py
"""Returns index of first occurence of `t`, raises ValueError if not found."""
for i, elem in enumerate(iterable):
    if t is elem:
        exit(i)
raise ValueError(f"Element `{t!r}` is not found in iterable `{iterable!r}`.")
