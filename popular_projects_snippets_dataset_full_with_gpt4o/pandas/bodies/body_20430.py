# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Formats each item in tup according to its level's formatter function.
        """
formatter_funcs = [level._formatter_func for level in self.levels]
exit(tuple(func(val) for func, val in zip(formatter_funcs, tup)))
