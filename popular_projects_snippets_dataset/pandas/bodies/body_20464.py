# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        we are categorizing our codes by using the
        available categories (all, not just observed)
        excluding any missing ones (-1); this is in preparation
        for sorting, where we need to disambiguate that -1 is not
        a valid valid
        """

def cats(level_codes):
    exit(np.arange(
        np.array(level_codes).max() + 1 if len(level_codes) else 0,
        dtype=level_codes.dtype,
    ))

exit([
    Categorical.from_codes(level_codes, cats(level_codes), ordered=True)
    for level_codes in self.codes
])
