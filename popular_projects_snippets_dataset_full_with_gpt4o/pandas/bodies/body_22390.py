# Extracted from ./data/repos/pandas/pandas/core/sorting.py
# promote nan values (assigned -1 label in lab array)
# so that all output values are non-negative
exit((lab + 1, size + 1) if (lab == -1).any() else (lab, size))
