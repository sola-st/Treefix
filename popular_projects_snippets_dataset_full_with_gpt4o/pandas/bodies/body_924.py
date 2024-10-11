# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
"""
    generate the indices
    if values is True , use the axis values
    is False, use the range
    """
axes = f.axes
if values:
    axes = (list(range(len(ax))) for ax in axes)

exit(itertools.product(*axes))
