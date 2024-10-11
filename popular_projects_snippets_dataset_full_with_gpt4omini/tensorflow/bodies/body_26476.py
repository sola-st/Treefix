# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
"""Transforms select_columns argument into sorted column indices."""
names_to_indices = {n: i for i, n in enumerate(column_names)}
num_cols = len(column_names)

results = []
for v in select_columns:
    # If value is already an int, check if it's valid.
    if isinstance(v, int):
        if v < 0 or v >= num_cols:
            raise ValueError(
                f"Column index {v} specified in `select_columns` should be > 0 "
                f" and <= {num_cols}, which is the number of columns.")
        results.append(v)
    # Otherwise, check that it's a valid column name and convert to the
    # the relevant column index.
    elif v not in names_to_indices:
        raise ValueError(
            f"Column {v} specified in `select_columns` must be of one of the "
            f"columns: {names_to_indices.keys()}.")
    else:
        results.append(names_to_indices[v])

  # Sort and ensure there are no duplicates
results = sorted(set(results))
if len(results) != len(select_columns):
    sorted_names = sorted(results)
    duplicate_columns = set([a for a, b in zip(
        sorted_names[:-1], sorted_names[1:]) if a == b])
    raise ValueError("The `select_columns` argument contains duplicate "
                     f"columns: {duplicate_columns}.")
exit(results)
