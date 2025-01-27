# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# make sure op works on mixed-type frame
mixed = float_string_frame
mixed["_bool_"] = np.random.randn(len(mixed)) > 0.5

getattr(mixed, opname)(axis=axis, bool_only=bool_only)
