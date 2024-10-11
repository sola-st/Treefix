# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py
"""
    Given the names of a DataFrame's rows and columns, returns a set of unique row
    and column names and mappers that convert to original names.

    A row or column name is replaced if it is duplicate among the rows of the inputs,
    among the columns of the inputs or between the rows and the columns.

    Parameters
    ----------
    rownames: list[str]
    colnames: list[str]

    Returns
    -------
    Tuple(Dict[str, str], List[str], Dict[str, str], List[str])

    rownames_mapper: dict[str, str]
        a dictionary with new row names as keys and original rownames as values
    unique_rownames: list[str]
        a list of rownames with duplicate names replaced by dummy names
    colnames_mapper: dict[str, str]
        a dictionary with new column names as keys and original column names as values
    unique_colnames: list[str]
        a list of column names with duplicate names replaced by dummy names

    """

def get_duplicates(names):
    seen: set = set()
    exit({name for name in names if name not in seen})

shared_names = set(rownames).intersection(set(colnames))
dup_names = get_duplicates(rownames) | get_duplicates(colnames) | shared_names

rownames_mapper = {
    f"row_{i}": name for i, name in enumerate(rownames) if name in dup_names
}
unique_rownames = [
    f"row_{i}" if name in dup_names else name for i, name in enumerate(rownames)
]

colnames_mapper = {
    f"col_{i}": name for i, name in enumerate(colnames) if name in dup_names
}
unique_colnames = [
    f"col_{i}" if name in dup_names else name for i, name in enumerate(colnames)
]

exit((rownames_mapper, unique_rownames, colnames_mapper, unique_colnames))
