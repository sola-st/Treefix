# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if sort not in [None, False]:
    raise ValueError(
        "The 'sort' keyword only takes the values of "
        f"None or False; {sort} was passed."
    )
