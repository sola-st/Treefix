# Extracted from ./data/repos/pandas/pandas/core/dtypes/base.py
"""
        Parameters
        ----------
        dtype : ExtensionDtype class
        """
if not issubclass(dtype, ExtensionDtype):
    raise ValueError("can only register pandas extension dtypes")

self.dtypes.append(dtype)
