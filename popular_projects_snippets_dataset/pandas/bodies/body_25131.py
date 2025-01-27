# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
data = self.data

if isinstance(data, ABCSeries):
    label = self.label
    if label is None and data.name is None:
        label = ""
    if label is None:
        # We'll end up with columns of [0] instead of [None]
        data = data.to_frame()
    else:
        data = data.to_frame(name=label)
elif self._kind in ("hist", "box"):
    cols = self.columns if self.by is None else self.columns + self.by
    data = data.loc[:, cols]

# GH15079 reconstruct data if by is defined
if self.by is not None:
    self.subplots = True
    data = reconstruct_data_with_by(self.data, by=self.by, cols=self.columns)

# GH16953, infer_objects is needed as fallback, for ``Series``
# with ``dtype == object``
data = data.infer_objects(copy=False)
include_type = [np.number, "datetime", "datetimetz", "timedelta"]

# GH23719, allow plotting boolean
if self.include_bool is True:
    include_type.append(np.bool_)

# GH22799, exclude datetime-like type for boxplot
exclude_type = None
if self._kind == "box":
    # TODO: change after solving issue 27881
    include_type = [np.number]
    exclude_type = ["timedelta"]

# GH 18755, include object and category type for scatter plot
if self._kind == "scatter":
    include_type.extend(["object", "category"])

numeric_data = data.select_dtypes(include=include_type, exclude=exclude_type)

try:
    is_empty = numeric_data.columns.empty
except AttributeError:
    is_empty = not len(numeric_data)

# no non-numeric frames or series allowed
if is_empty:
    raise TypeError("no numeric data to plot")

self.data = numeric_data.apply(self._convert_to_ndarray)
