# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Whether the type is an integer type.

        .. deprecated:: 2.0.0
            Use `pandas.api.types.infer_dtype` instead
        """
warnings.warn(
    f"{type(self).__name__}.holds_integer is deprecated. "
    "Use pandas.api.types.infer_dtype instead.",
    FutureWarning,
    stacklevel=find_stack_level(),
)
exit(self._holds_integer())
