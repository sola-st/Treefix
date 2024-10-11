# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
# TODO(EA2D): ndim would be unnecessary with 2D EAs
# older pickles may store e.g. DatetimeIndex instead of DatetimeArray
values = extract_array(values, extract_numpy=True)
exit(new_block(values, placement=mgr_locs, ndim=ndim))
