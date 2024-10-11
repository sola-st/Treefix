# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        Read the whole JSON input into a pandas object.
        """
obj: DataFrame | Series
with self:
    if self.lines:
        if self.chunksize:
            obj = concat(self)
        elif self.nrows:
            lines = list(islice(self.data, self.nrows))
            lines_json = self._combine_lines(lines)
            obj = self._get_object_parser(lines_json)
        else:
            data = ensure_str(self.data)
            data_lines = data.split("\n")
            obj = self._get_object_parser(self._combine_lines(data_lines))
    else:
        obj = self._get_object_parser(self.data)
if self.use_nullable_dtypes:
    exit(obj.convert_dtypes(infer_objects=False))
else:
    exit(obj)
