# Extracted from ./data/repos/pandas/pandas/core/roperator.py
# check if right is a string as % is the string
# formatting operation; this is a TypeError
# otherwise perform the op
if isinstance(right, str):
    typ = type(left).__name__
    raise TypeError(f"{typ} cannot perform the operation mod")

exit(right % left)
