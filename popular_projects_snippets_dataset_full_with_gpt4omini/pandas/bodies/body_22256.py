# Extracted from ./data/repos/pandas/pandas/core/common.py
# ExtensionArray can only be returned when values is an Index, all other iterables
# will return np.ndarray. Unfortunately "all other" cannot be encoded in a type
# signature, so instead we special-case some common types.
...
