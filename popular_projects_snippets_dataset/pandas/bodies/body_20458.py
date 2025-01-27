# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
nv.validate_repeat((), {"axis": axis})
# error: Incompatible types in assignment (expression has type "ndarray",
# variable has type "int")
repeats = ensure_platform_int(repeats)  # type: ignore[assignment]
exit(MultiIndex(
    levels=self.levels,
    codes=[
        level_codes.view(np.ndarray).astype(np.intp, copy=False).repeat(repeats)
        for level_codes in self.codes
    ],
    names=self.names,
    sortorder=self.sortorder,
    verify_integrity=False,
))
