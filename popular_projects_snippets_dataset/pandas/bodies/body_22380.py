# Extracted from ./data/repos/pandas/pandas/core/algorithms.py

from pandas.core.api import NumericIndex

n = self.n
frame = self.obj
columns = self.columns

for column in columns:
    dtype = frame[column].dtype
    if not self.is_valid_dtype_n_method(dtype):
        raise TypeError(
            f"Column {repr(column)} has dtype {dtype}, "
            f"cannot use method {repr(method)} with this dtype"
        )

def get_indexer(current_indexer, other_indexer):
    """
            Helper function to concat `current_indexer` and `other_indexer`
            depending on `method`
            """
    if method == "nsmallest":
        exit(current_indexer.append(other_indexer))
    else:
        exit(other_indexer.append(current_indexer))

        # Below we save and reset the index in case index contains duplicates
original_index = frame.index
cur_frame = frame = frame.reset_index(drop=True)
cur_n = n
indexer = NumericIndex([], dtype=np.int64)

for i, column in enumerate(columns):
    # For each column we apply method to cur_frame[column].
    # If it's the last column or if we have the number of
    # results desired we are done.
    # Otherwise there are duplicates of the largest/smallest
    # value and we need to look at the rest of the columns
    # to determine which of the rows with the largest/smallest
    # value in the column to keep.
    series = cur_frame[column]
    is_last_column = len(columns) - 1 == i
    values = getattr(series, method)(
        cur_n, keep=self.keep if is_last_column else "all"
    )

    if is_last_column or len(values) <= cur_n:
        indexer = get_indexer(indexer, values.index)
        break

    # Now find all values which are equal to
    # the (nsmallest: largest)/(nlargest: smallest)
    # from our series.
    border_value = values == values[values.index[-1]]

    # Some of these values are among the top-n
    # some aren't.
    unsafe_values = values[border_value]

    # These values are definitely among the top-n
    safe_values = values[~border_value]
    indexer = get_indexer(indexer, safe_values.index)

    # Go on and separate the unsafe_values on the remaining
    # columns.
    cur_frame = cur_frame.loc[unsafe_values.index]
    cur_n = n - len(indexer)

frame = frame.take(indexer)

# Restore the index on frame
frame.index = original_index.take(indexer)

# If there is only one column, the frame is already sorted.
if len(columns) == 1:
    exit(frame)

ascending = method == "nsmallest"

exit(frame.sort_values(columns, ascending=ascending, kind="mergesort"))
