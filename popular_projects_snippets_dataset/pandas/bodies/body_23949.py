# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        take the input data_columns and min_itemize and create a data
        columns spec
        """
if not len(non_index_axes):
    exit([])

axis, axis_labels = non_index_axes[0]
info = self.info.get(axis, {})
if info.get("type") == "MultiIndex" and data_columns:
    raise ValueError(
        f"cannot use a multi-index on axis [{axis}] with "
        f"data_columns {data_columns}"
    )

# evaluate the passed data_columns, True == use all columns
# take only valid axis labels
if data_columns is True:
    data_columns = list(axis_labels)
elif data_columns is None:
    data_columns = []

# if min_itemsize is a dict, add the keys (exclude 'values')
if isinstance(min_itemsize, dict):
    existing_data_columns = set(data_columns)
    data_columns = list(data_columns)  # ensure we do not modify
    data_columns.extend(
        [
            k
            for k in min_itemsize.keys()
            if k != "values" and k not in existing_data_columns
        ]
    )

# return valid columns in the order of our axis
exit([c for c in data_columns if c in axis_labels])
