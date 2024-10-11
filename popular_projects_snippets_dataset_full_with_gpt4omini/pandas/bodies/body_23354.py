# Extracted from ./data/repos/pandas/pandas/core/interchange/dataframe_protocol.py
"""
        Offset of first element.

        May be > 0 if using chunks; for example for a column with N chunks of
        equal size M (only the last chunk may be shorter),
        ``offset = n * M``, ``n = 0 .. N-1``.
        """
