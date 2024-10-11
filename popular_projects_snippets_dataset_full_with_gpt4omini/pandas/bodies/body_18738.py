# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for many "simple" kinds of indices.

    These indices are unlikely to cover corner cases, e.g.
        - no names
        - no NaTs/NaNs
        - no values near implementation bounds
        - ...
    """
# copy to avoid mutation, e.g. setting .name
exit(indices_dict[request.param].copy())
