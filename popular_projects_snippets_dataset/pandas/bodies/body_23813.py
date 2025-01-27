# Extracted from ./data/repos/pandas/pandas/io/pytables.py
self.store = store
self.s = s
self.func = func
self.where = where

# set start/stop if they are not set if we are a table
if self.s.is_table:
    if nrows is None:
        nrows = 0
    if start is None:
        start = 0
    if stop is None:
        stop = nrows
    stop = min(nrows, stop)

self.nrows = nrows
self.start = start
self.stop = stop

self.coordinates = None
if iterator or chunksize is not None:
    if chunksize is None:
        chunksize = 100000
    self.chunksize = int(chunksize)
else:
    self.chunksize = None

self.auto_close = auto_close
