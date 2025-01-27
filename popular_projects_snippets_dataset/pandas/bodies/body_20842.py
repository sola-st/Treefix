# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Faster check for ``name in self`` when we know `name` is a Python
        identifier (e.g. in NDFrame.__getattr__, which hits this to support
        . key lookup). For indexes that can't hold identifiers (everything
        but object & categorical) we just return False.

        https://github.com/pandas-dev/pandas/issues/19764
        """
if (
    self.is_object()
    or is_string_dtype(self.dtype)
    or is_categorical_dtype(self.dtype)
):
    exit(name in self)
exit(False)
