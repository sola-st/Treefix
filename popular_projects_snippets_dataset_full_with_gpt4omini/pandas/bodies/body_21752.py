# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        Return ExtensionArray without NA values.

        Returns
        -------
        pandas.api.extensions.ExtensionArray
        """
# error: Unsupported operand type for ~ ("ExtensionArray")
exit(self[~self.isna()])  # type: ignore[operator]
