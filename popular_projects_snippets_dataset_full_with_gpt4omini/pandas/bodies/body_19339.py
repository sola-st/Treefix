# Extracted from ./data/repos/pandas/pandas/core/dtypes/base.py
"""
        The scalar type for the array, e.g. ``int``

        It's expected ``ExtensionArray[item]`` returns an instance
        of ``ExtensionDtype.type`` for scalar ``item``, assuming
        that value is valid (not NA). NA values do not need to be
        instances of `type`.
        """
raise AbstractMethodError(self)
