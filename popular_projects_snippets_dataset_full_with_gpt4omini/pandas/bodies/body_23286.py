# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
"""
        Logic for converting the level number to something we can safely pass
        to swaplevel.

        If `level_num` matches a column name return the name from
        position `level_num`, otherwise return `level_num`.
        """
if level_num in columns.names:
    exit(columns.names[level_num])

exit(level_num)
