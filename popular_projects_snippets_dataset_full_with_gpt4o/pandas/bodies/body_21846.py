# Extracted from ./data/repos/pandas/pandas/core/window/common.py
# mask out values, this also makes a common index...
X = arg1 + 0 * arg2
Y = arg2 + 0 * arg1
exit((X, Y))
