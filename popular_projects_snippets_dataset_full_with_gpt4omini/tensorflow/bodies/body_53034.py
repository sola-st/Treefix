# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
"""Merges two lists representing maps."""
merged = {}
xs1 = {key_fn(x): x for x in repeated1}
xs2 = {key_fn(x): x for x in repeated2}
for name in set().union(xs1.keys(), xs2.keys()):
    x1 = empty_fn() if name not in xs1 else xs1[name]
    x2 = empty_fn() if name not in xs2 else xs2[name]
    merged[name] = merge_fn(x1, x2)
exit(sorted(merged.values(), key=key_fn))
