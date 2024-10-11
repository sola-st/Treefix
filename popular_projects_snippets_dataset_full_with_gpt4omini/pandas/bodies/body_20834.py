# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
# We return the TypeError so that we can raise it from the constructor
#  in order to keep mypy happy
raise TypeError(
    f"{cls.__name__}(...) must be called with a collection of some "
    f"kind, {repr(data)} was passed"
)
