# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# covers GH#11245
assert Series([], dtype=dtype).min(skipna=skipna) is NaT
assert Series([], dtype=dtype).max(skipna=skipna) is NaT
