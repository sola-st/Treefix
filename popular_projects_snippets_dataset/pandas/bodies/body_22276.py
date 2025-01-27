# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    Check the length of data matches the length of the index.
    """
if len(data) != len(index):
    raise ValueError(
        "Length of values "
        f"({len(data)}) "
        "does not match length of index "
        f"({len(index)})"
    )
