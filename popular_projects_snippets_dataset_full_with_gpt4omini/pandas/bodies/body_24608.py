# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
if self.index:
    exit(getattr(self.data_index, "nlevels", 1))
else:
    exit(0)
