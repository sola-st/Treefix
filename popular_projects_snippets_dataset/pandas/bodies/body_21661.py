# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Returns day, hour, minute, second, millisecond or microsecond
        """
# error: Item "None" of "Optional[Any]" has no attribute "attrname"
exit(self._resolution_obj.attrname)  # type: ignore[union-attr]
