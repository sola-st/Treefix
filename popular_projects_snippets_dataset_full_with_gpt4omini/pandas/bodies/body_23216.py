# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py

columns = left.columns.union(right.columns)

for i in ["_left_indicator", "_right_indicator"]:
    if i in columns:
        raise ValueError(
            "Cannot use `indicator=True` option when "
            f"data contains a column named {i}"
        )
if self._indicator_name in columns:
    raise ValueError(
        "Cannot use name of an existing column for indicator column"
    )

left = left.copy()
right = right.copy()

left["_left_indicator"] = 1
left["_left_indicator"] = left["_left_indicator"].astype("int8")

right["_right_indicator"] = 2
right["_right_indicator"] = right["_right_indicator"].astype("int8")

exit((left, right))
