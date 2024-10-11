# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
"""
        Returns a numpy character array of the column types:
           s (string) or d (double)
        """
exit(np.asarray(self._column_types, dtype=np.dtype("S1")))
