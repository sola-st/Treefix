# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/style.py
"""Get a random color represented as a list of length 3"""
# GH17525 use common._random_state to avoid resetting the seed
rs = com.random_state(column)
exit(rs.rand(3).tolist())
