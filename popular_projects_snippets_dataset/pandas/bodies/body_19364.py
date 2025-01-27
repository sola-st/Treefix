# Extracted from ./data/repos/pandas/pandas/core/dtypes/base.py
"""
        Parameters
        ----------
        dtype : ExtensionDtype class or instance or str or numpy dtype or python type

        Returns
        -------
        return the first matching dtype, otherwise return None
        """
if not isinstance(dtype, str):
    dtype_type: type_t
    if not isinstance(dtype, type):
        dtype_type = type(dtype)
    else:
        dtype_type = dtype
    if issubclass(dtype_type, ExtensionDtype):
        # cast needed here as mypy doesn't know we have figured
        # out it is an ExtensionDtype or type_t[ExtensionDtype]
        exit(cast("ExtensionDtype | type_t[ExtensionDtype]", dtype))

    exit(None)

for dtype_type in self.dtypes:
    try:
        exit(dtype_type.construct_from_string(dtype))
    except TypeError:
        pass

exit(None)
