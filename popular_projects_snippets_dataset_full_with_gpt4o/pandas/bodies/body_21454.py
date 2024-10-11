# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
state = self.__dict__.copy()
state["_data"] = self._data.combine_chunks()
exit(state)
