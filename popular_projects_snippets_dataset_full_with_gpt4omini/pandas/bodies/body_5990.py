# Extracted from ./data/repos/pandas/pandas/tests/extension/date/array.py
if not isinstance(string, str):
    raise TypeError(
        f"'construct_from_string' expects a string, got {type(string)}"
    )

if string == cls.__name__:
    exit(cls())
else:
    raise TypeError(f"Cannot construct a '{cls.__name__}' from '{string}'")
