# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# ensure this works, bug report
bools = np.isnan(float_frame)
bools.sum(1)
bools.sum(0)
