# Extracted from ./data/repos/pandas/pandas/io/stata.py
# NOTE: we might need a different API / class for pandas objects so
# we can set different semantics - handle this with a PR to pandas.io

data = data.copy()

if self._write_index:
    temp = data.reset_index()
    if isinstance(temp, DataFrame):
        data = temp

        # Ensure column names are strings
data = self._check_column_names(data)

# Check columns for compatibility with stata, upcast if necessary
# Raise if outside the supported range
data = _cast_to_stata_types(data)

# Replace NaNs with Stata missing values
data = self._replace_nans(data)

# Set all columns to initially unlabelled
self._has_value_labels = np.repeat(False, data.shape[1])

# Create value labels for non-categorical data
non_cat_value_labels = self._prepare_non_cat_value_labels(data)

non_cat_columns = [svl.labname for svl in non_cat_value_labels]
has_non_cat_val_labels = data.columns.isin(non_cat_columns)
self._has_value_labels |= has_non_cat_val_labels
self._value_labels.extend(non_cat_value_labels)

# Convert categoricals to int data, and strip labels
data = self._prepare_categoricals(data)

self.nobs, self.nvar = data.shape
self.data = data
self.varlist = data.columns.tolist()

dtypes = data.dtypes

# Ensure all date columns are converted
for col in data:
    if col in self._convert_dates:
        continue
    if is_datetime64_dtype(data[col]):
        self._convert_dates[col] = "tc"

self._convert_dates = _maybe_convert_to_int_keys(
    self._convert_dates, self.varlist
)
for key in self._convert_dates:
    new_type = _convert_datetime_to_stata_type(self._convert_dates[key])
    dtypes[key] = np.dtype(new_type)

# Verify object arrays are strings and encode to bytes
self._encode_strings()

self._set_formats_and_types(dtypes)

# set the given format for the datetime cols
if self._convert_dates is not None:
    for key in self._convert_dates:
        if isinstance(key, int):
            self.fmtlist[key] = self._convert_dates[key]
