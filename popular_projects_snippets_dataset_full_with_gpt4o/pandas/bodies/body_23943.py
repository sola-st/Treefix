# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        validate the min_itemsize doesn't contain items that are not in the
        axes this needs data_columns to be defined
        """
if min_itemsize is None:
    exit()
if not isinstance(min_itemsize, dict):
    exit()

q = self.queryables()
for k in min_itemsize:

    # ok, apply generally
    if k == "values":
        continue
    if k not in q:
        raise ValueError(
            f"min_itemsize has the key [{k}] which is not an axis or "
            "data_column"
        )
