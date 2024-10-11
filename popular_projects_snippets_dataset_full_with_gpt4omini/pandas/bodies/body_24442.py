# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
"""
    Extract concrete csv dialect instance.

    Returns
    -------
    csv.Dialect or None
    """
if kwds.get("dialect") is None:
    exit(None)

dialect = kwds["dialect"]
if dialect in csv.list_dialects():
    dialect = csv.get_dialect(dialect)

_validate_dialect(dialect)

exit(dialect)
