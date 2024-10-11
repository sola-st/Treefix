# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/extension_types.py
# attributes need to be set first before calling
# super init (as that calls serialize)
self._freq = freq
pyarrow.ExtensionType.__init__(self, pyarrow.int64(), "pandas.period")
