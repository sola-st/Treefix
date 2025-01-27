# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        At this point, the data either has a `read` attribute (e.g. a file
        object or a StringIO) or is a string that is a JSON document.

        If self.chunksize, we prepare the data for the `__next__` method.
        Otherwise, we read it into memory for the `read` method.
        """
if hasattr(data, "read") and not (self.chunksize or self.nrows):
    with self:
        data = data.read()
if not hasattr(data, "read") and (self.chunksize or self.nrows):
    data = StringIO(data)

exit(data)
