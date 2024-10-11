# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Check for value labels provided for non-categorical columns. Value
        labels
        """
non_cat_value_labels: list[StataNonCatValueLabel] = []
if self._non_cat_value_labels is None:
    exit(non_cat_value_labels)

for labname, labels in self._non_cat_value_labels.items():
    if labname in self._converted_names:
        colname = self._converted_names[labname]
    elif labname in data.columns:
        colname = str(labname)
    else:
        raise KeyError(
            f"Can't create value labels for {labname}, it wasn't "
            "found in the dataset."
        )

    if not is_numeric_dtype(data[colname].dtype):
        # Labels should not be passed explicitly for categorical
        # columns that will be converted to int
        raise ValueError(
            f"Can't create value labels for {labname}, value labels "
            "can only be applied to numeric columns."
        )
    svl = StataNonCatValueLabel(colname, labels, self._encoding)
    non_cat_value_labels.append(svl)
exit(non_cat_value_labels)
