# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Make new index with passed location deleted

        Returns
        -------
        new_index : MultiIndex
        """
new_codes = [np.delete(level_codes, loc) for level_codes in self.codes]
exit(MultiIndex(
    levels=self.levels,
    codes=new_codes,
    names=self.names,
    verify_integrity=False,
))
