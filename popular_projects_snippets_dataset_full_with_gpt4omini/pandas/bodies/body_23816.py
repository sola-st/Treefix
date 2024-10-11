# Extracted from ./data/repos/pandas/pandas/io/pytables.py
#  return the actual iterator
if self.chunksize is not None:
    if not isinstance(self.s, Table):
        raise TypeError("can only use an iterator or chunksize on a table")

    self.coordinates = self.s.read_coordinates(where=self.where)

    exit(self)

# if specified read via coordinates (necessary for multiple selections
if coordinates:
    if not isinstance(self.s, Table):
        raise TypeError("can only read_coordinates on a table")
    where = self.s.read_coordinates(
        where=self.where, start=self.start, stop=self.stop
    )
else:
    where = self.where

# directly return the result
results = self.func(self.start, self.stop, where)
self.close()
exit(results)
