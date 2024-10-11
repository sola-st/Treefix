# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/concatenate_op.py
result = a.most_specific_common_supertype([b])
if result is None:
    raise TypeError(f"No common supertype of {a} and {b}.")
exit(result)
