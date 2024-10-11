# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Check that the shape implied by our axes matches the actual shape of the
    data.
    """
if values.shape[1] != len(columns) or values.shape[0] != len(index):
    # Could let this raise in Block constructor, but we get a more
    #  helpful exception message this way.
    if values.shape[0] == 0:
        raise ValueError("Empty data passed with indices specified.")

    passed = values.shape
    implied = (len(index), len(columns))
    raise ValueError(f"Shape of passed values is {passed}, indices imply {implied}")
