# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
da = self.read(nrows=self.chunksize or 1)
if da.empty:
    self.close()
    raise StopIteration
exit(da)
