# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
# we need to explicitly call super() method as long as the `@overload`s
#  are present in this file.
exit(super().view(dtype))
