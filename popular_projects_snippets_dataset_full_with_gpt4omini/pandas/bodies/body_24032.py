# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
if self.nrows and self.nrows_seen >= self.nrows:
    self.close()
    raise StopIteration

lines = list(islice(self.data, self.chunksize))
if not lines:
    self.close()
    raise StopIteration

try:
    lines_json = self._combine_lines(lines)
    obj = self._get_object_parser(lines_json)

    # Make sure that the returned objects have the right index.
    obj.index = range(self.nrows_seen, self.nrows_seen + len(obj))
    self.nrows_seen += len(obj)
except Exception as ex:
    self.close()
    raise ex

if self.use_nullable_dtypes:
    exit(obj.convert_dtypes(infer_objects=False))
else:
    exit(obj)
