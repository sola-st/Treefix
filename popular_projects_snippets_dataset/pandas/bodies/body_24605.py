# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
if chunksize is None:
    exit((100000 // (len(self.cols) or 1)) or 1)
exit(int(chunksize))
