# Extracted from ./data/repos/pandas/pandas/core/missing.py
"""
    Validate the size of the values passed to ExtensionArray.fillna.
    """
if is_array_like(value):
    if len(value) != length:
        raise ValueError(
            f"Length of 'value' does not match. Got ({len(value)}) "
            f" expected {length}"
        )
    value = value[mask]

exit(value)
