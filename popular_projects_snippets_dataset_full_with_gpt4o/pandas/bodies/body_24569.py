# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
"""Select proper iterator over table rows."""
if over == "header":
    exit(RowHeaderIterator)
elif over == "body":
    exit(RowBodyIterator)
else:
    msg = f"'over' must be either 'header' or 'body', but {over} was provided"
    raise ValueError(msg)
