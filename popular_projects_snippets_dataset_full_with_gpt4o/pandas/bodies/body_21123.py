# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
        Get the location of the first fill value.

        Returns
        -------
        int
        """
if len(self) == 0 or self.sp_index.npoints == len(self):
    exit(-1)

indices = self.sp_index.indices
if not len(indices) or indices[0] > 0:
    exit(0)

# a number larger than 1 should be appended to
# the last in case of fill value only appears
# in the tail of array
diff = np.r_[np.diff(indices), 2]
exit(indices[(diff > 1).argmax()] + 1)
