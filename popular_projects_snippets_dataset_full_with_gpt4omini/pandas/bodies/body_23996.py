# Extracted from ./data/repos/pandas/pandas/io/pytables.py
self.table = table
self.where = where
self.start = start
self.stop = stop
self.condition = None
self.filter = None
self.terms = None
self.coordinates = None

if is_list_like(where):

    # see if we have a passed coordinate like
    with suppress(ValueError):
        inferred = lib.infer_dtype(where, skipna=False)
        if inferred in ("integer", "boolean"):
            where = np.asarray(where)
            if where.dtype == np.bool_:
                start, stop = self.start, self.stop
                if start is None:
                    start = 0
                if stop is None:
                    stop = self.table.nrows
                self.coordinates = np.arange(start, stop)[where]
            elif issubclass(where.dtype.type, np.integer):
                if (self.start is not None and (where < self.start).any()) or (
                    self.stop is not None and (where >= self.stop).any()
                ):
                    raise ValueError(
                        "where must have index locations >= start and < stop"
                    )
                self.coordinates = where

if self.coordinates is None:

    self.terms = self.generate(where)

    # create the numexpr & the filter
    if self.terms is not None:
        self.condition, self.filter = self.terms.evaluate()
