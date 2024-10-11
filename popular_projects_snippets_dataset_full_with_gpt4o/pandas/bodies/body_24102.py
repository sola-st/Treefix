# Extracted from ./data/repos/pandas/pandas/io/excel/_util.py
"""
    Forward fill blank entries in row but only inside the same parent index.

    Used for creating headers in Multiindex.

    Parameters
    ----------
    row : list
        List of items in a single row.
    control_row : list of bool
        Helps to determine if particular column is in same parent index as the
        previous value. Used to stop propagation of empty cells between
        different indexes.

    Returns
    -------
    Returns changed row and control_row
    """
last = row[0]
for i in range(1, len(row)):
    if not control_row[i]:
        last = row[i]

    if row[i] == "" or row[i] is None:
        row[i] = last
    else:
        control_row[i] = False
        last = row[i]

exit((row, control_row))
