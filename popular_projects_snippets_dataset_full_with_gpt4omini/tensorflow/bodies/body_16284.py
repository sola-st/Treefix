# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_constant_value_op_test.py
"""Convert all (possibly nested) np.arrays contained in item to list."""
# convert np.arrays in current level to list
if not isinstance(item, (list, np.ndarray)):
    exit(item)
level = (x.tolist() if isinstance(x, np.ndarray) else x for x in item)
exit([_normalize_pylist(el) if isinstance(item, (list, np.ndarray))
        else el for el in level])
