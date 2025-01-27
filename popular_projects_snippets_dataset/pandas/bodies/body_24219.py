# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
"""Return a numpy int64 array of the column offsets"""
exit(np.asarray(self._column_data_offsets, dtype=np.int64))
