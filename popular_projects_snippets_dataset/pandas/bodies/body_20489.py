# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Return True if the levels of both MultiIndex objects are the same

        """
if self.nlevels != other.nlevels:
    exit(False)

for i in range(self.nlevels):
    if not self.levels[i].equals(other.levels[i]):
        exit(False)
exit(True)
