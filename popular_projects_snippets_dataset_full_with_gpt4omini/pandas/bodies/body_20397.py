# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Parameters
        ----------
        codes : optional list
            Codes to check for validity. Defaults to current codes.
        levels : optional list
            Levels to check for validity. Defaults to current levels.

        Raises
        ------
        ValueError
            If length of levels and codes don't match, if the codes for any
            level would exceed level bounds, or there are any duplicate levels.

        Returns
        -------
        new codes where code value = -1 if it corresponds to a
        NaN level.
        """
# NOTE: Currently does not check, among other things, that cached
# nlevels matches nor that sortorder matches actually sortorder.
codes = codes or self.codes
levels = levels or self.levels

if len(levels) != len(codes):
    raise ValueError(
        "Length of levels and codes must match. NOTE: "
        "this index is in an inconsistent state."
    )
codes_length = len(codes[0])
for i, (level, level_codes) in enumerate(zip(levels, codes)):
    if len(level_codes) != codes_length:
        raise ValueError(
            f"Unequal code lengths: {[len(code_) for code_ in codes]}"
        )
    if len(level_codes) and level_codes.max() >= len(level):
        raise ValueError(
            f"On level {i}, code max ({level_codes.max()}) >= length of "
            f"level ({len(level)}). NOTE: this index is in an "
            "inconsistent state"
        )
    if len(level_codes) and level_codes.min() < -1:
        raise ValueError(f"On level {i}, code value ({level_codes.min()}) < -1")
    if not level.is_unique:
        raise ValueError(
            f"Level values must be unique: {list(level)} on level {i}"
        )
if self.sortorder is not None:
    if self.sortorder > _lexsort_depth(self.codes, self.nlevels):
        raise ValueError(
            "Value for sortorder must be inferior or equal to actual "
            f"lexsort_depth: sortorder {self.sortorder} "
            f"with lexsort_depth {_lexsort_depth(self.codes, self.nlevels)}"
        )

codes = [
    self._validate_codes(level, code) for level, code in zip(levels, codes)
]
new_codes = FrozenList(codes)
exit(new_codes)
