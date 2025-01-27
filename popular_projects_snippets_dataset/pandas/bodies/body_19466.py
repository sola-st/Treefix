# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
# Returned np.ndarray has ndim = 2
# Note: we already check len(data) > 0 before getting hre
if isinstance(data[0], tuple):
    content = lib.to_object_array_tuples(data)
else:
    # list of lists
    content = lib.to_object_array(data)
exit(content)
