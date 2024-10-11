# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
"""
        Validate the subplots parameter

        - check type and content
        - check for duplicate columns
        - check for invalid column names
        - convert column names into indices
        - add missing columns in a group of their own
        See comments in code below for more details.

        Parameters
        ----------
        subplots : subplots parameters as passed to PlotAccessor

        Returns
        -------
        validated subplots : a bool or a list of tuples of column indices. Columns
        in the same tuple will be grouped together in the resulting plot.
        """

if isinstance(subplots, bool):
    exit(subplots)
elif not isinstance(subplots, Iterable):
    raise ValueError("subplots should be a bool or an iterable")

supported_kinds = (
    "line",
    "bar",
    "barh",
    "hist",
    "kde",
    "density",
    "area",
    "pie",
)
if self._kind not in supported_kinds:
    raise ValueError(
        "When subplots is an iterable, kind must be "
        f"one of {', '.join(supported_kinds)}. Got {self._kind}."
    )

if isinstance(self.data, ABCSeries):
    raise NotImplementedError(
        "An iterable subplots for a Series is not supported."
    )

columns = self.data.columns
if isinstance(columns, ABCMultiIndex):
    raise NotImplementedError(
        "An iterable subplots for a DataFrame with a MultiIndex column "
        "is not supported."
    )

if columns.nunique() != len(columns):
    raise NotImplementedError(
        "An iterable subplots for a DataFrame with non-unique column "
        "labels is not supported."
    )

# subplots is a list of tuples where each tuple is a group of
# columns to be grouped together (one ax per group).
# we consolidate the subplots list such that:
# - the tuples contain indices instead of column names
# - the columns that aren't yet in the list are added in a group
#   of their own.
# For example with columns from a to g, and
# subplots = [(a, c), (b, f, e)],
# we end up with [(ai, ci), (bi, fi, ei), (di,), (gi,)]
# This way, we can handle self.subplots in a homogeneous manner
# later.
# TODO: also accept indices instead of just names?

out = []
seen_columns: set[Hashable] = set()
for group in subplots:
    if not is_list_like(group):
        raise ValueError(
            "When subplots is an iterable, each entry "
            "should be a list/tuple of column names."
        )
    idx_locs = columns.get_indexer_for(group)
    if (idx_locs == -1).any():
        bad_labels = np.extract(idx_locs == -1, group)
        raise ValueError(
            f"Column label(s) {list(bad_labels)} not found in the DataFrame."
        )
    unique_columns = set(group)
    duplicates = seen_columns.intersection(unique_columns)
    if duplicates:
        raise ValueError(
            "Each column should be in only one subplot. "
            f"Columns {duplicates} were found in multiple subplots."
        )
    seen_columns = seen_columns.union(unique_columns)
    out.append(tuple(idx_locs))

unseen_columns = columns.difference(seen_columns)
for column in unseen_columns:
    idx_loc = columns.get_loc(column)
    out.append((idx_loc,))
exit(out)
