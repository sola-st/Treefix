# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
if size is None:
    size = self.chunksize
if self.nrows is not None:
    if self._currow >= self.nrows:
        raise StopIteration
    size = min(size, self.nrows - self._currow)
exit(self.read(nrows=size))
