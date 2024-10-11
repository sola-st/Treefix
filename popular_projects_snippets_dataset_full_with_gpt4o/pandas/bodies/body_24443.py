# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
"""
    Validate csv dialect instance.

    Raises
    ------
    ValueError
        If incorrect dialect is provided.
    """
for param in MANDATORY_DIALECT_ATTRS:
    if not hasattr(dialect, param):
        raise ValueError(f"Invalid dialect {dialect} provided")
