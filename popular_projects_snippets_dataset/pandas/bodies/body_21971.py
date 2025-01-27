# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""
        Returns
        -------
        Generator yielding subsetted objects
        """
ids, _, ngroups = self.group_info
exit(get_splitter(data, ids, ngroups, axis=axis))
