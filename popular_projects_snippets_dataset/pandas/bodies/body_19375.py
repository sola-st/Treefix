# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
# for pickle compat. __get_state__ is defined in the
# PandasExtensionDtype superclass and uses the public properties to
# pickle -> need to set the settable private ones here (see GH26067)
self._categories = state.pop("categories", None)
self._ordered = state.pop("ordered", False)
