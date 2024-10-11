# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
if not isinstance(other, ArrowExtensionArray):
    exit(False)
# I'm told that pyarrow makes __eq__ behave like pandas' equals;
#  TODO: is this documented somewhere?
exit(self._data == other._data)
