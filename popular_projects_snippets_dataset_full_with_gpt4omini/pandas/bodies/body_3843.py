# Extracted from ./data/repos/pandas/pandas/tests/frame/conftest.py
"""
    Fixture for DataFrame with uint64 values

    Columns are ['A', 'B']
    """
exit(DataFrame(
    {"A": np.arange(3), "B": [2**63, 2**63 + 5, 2**63 + 10]}, dtype=np.uint64
))
