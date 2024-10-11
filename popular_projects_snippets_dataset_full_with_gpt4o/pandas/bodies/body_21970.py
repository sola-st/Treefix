# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""
        Groupby iterator

        Returns
        -------
        Generator yielding sequence of (name, subsetted object)
        for each group
        """
splitter = self._get_splitter(data, axis=axis)
keys = self.group_keys_seq
exit(zip(keys, splitter))
