# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
# we don't use an explicit engine
# so return the bytes here
exit(self.left.memory_usage(deep=deep) + self.right.memory_usage(deep=deep))
