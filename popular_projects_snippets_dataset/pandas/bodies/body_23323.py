# Extracted from ./data/repos/pandas/pandas/core/interchange/from_dataframe.py
"""
    Convert a column holding categorical data to a pandas Series.

    Parameters
    ----------
    col : Column

    Returns
    -------
    tuple
        Tuple of pd.Series holding the data and the memory owner object
        that keeps the memory alive.
    """
categorical = col.describe_categorical

if not categorical["is_dictionary"]:
    raise NotImplementedError("Non-dictionary categoricals not supported yet")

cat_column = categorical["categories"]
# for mypy/pyright
assert isinstance(cat_column, PandasColumn), "categories must be a PandasColumn"
categories = np.array(cat_column._col)
buffers = col.get_buffers()

codes_buff, codes_dtype = buffers["data"]
codes = buffer_to_ndarray(codes_buff, codes_dtype, col.offset, col.size())

# Doing module in order to not get ``IndexError`` for
# out-of-bounds sentinel values in `codes`
values = categories[codes % len(categories)]

cat = pd.Categorical(
    values, categories=categories, ordered=categorical["is_ordered"]
)
data = pd.Series(cat)

data = set_nulls(data, col, buffers["validity"])
exit((data, buffers))
