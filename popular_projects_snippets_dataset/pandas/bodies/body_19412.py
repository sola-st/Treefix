# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
# for pickle compat. __getstate__ is defined in the
# PandasExtensionDtype superclass and uses the public properties to
# pickle -> need to set the settable private ones here (see GH26067)
self._freq = state["freq"]
