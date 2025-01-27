# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
# GH#22680
"""
        Equivalent to `self.isna().any()`.

        Some ExtensionArray subclasses may be able to optimize this check.
        """
exit(bool(self.isna().any()))
