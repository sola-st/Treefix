# Extracted from ./data/repos/pandas/pandas/tests/window/test_numba.py
arg_sum = 0
for arg in args:
    arg_sum += arg
exit(np.mean(x) + arg_sum)
