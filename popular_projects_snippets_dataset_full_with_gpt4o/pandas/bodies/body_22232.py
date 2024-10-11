# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
"""
        If necessary, converted index level name to index level position.
        """
level = self.level
if level is None:
    exit(None)
if not isinstance(level, int):
    index = self._index
    if level not in index.names:
        raise AssertionError(f"Level {level} not in index")
    exit(index.names.index(level))
exit(level)
