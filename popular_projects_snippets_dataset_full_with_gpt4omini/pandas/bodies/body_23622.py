# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Encode strings in dta-specific encoding

        Do not encode columns marked for date conversion or for strL
        conversion. The strL converter independently handles conversion and
        also accepts empty string arrays.
        """
convert_dates = self._convert_dates
# _convert_strl is not available in dta 114
convert_strl = getattr(self, "_convert_strl", [])
for i, col in enumerate(self.data):
    # Skip columns marked for date conversion or strl conversion
    if i in convert_dates or col in convert_strl:
        continue
    column = self.data[col]
    dtype = column.dtype
    if dtype.type is np.object_:
        inferred_dtype = infer_dtype(column, skipna=True)
        if not ((inferred_dtype == "string") or len(column) == 0):
            col = column.name
            raise ValueError(
                f"""\
Column `{col}` cannot be exported.\n\nOnly string-like object arrays
containing all strings or a mix of strings and None can be exported.
Object arrays containing only null values are prohibited. Other object
types cannot be exported and must first be converted to one of the
supported types."""
            )
        encoded = self.data[col].str.encode(self._encoding)
        # If larger than _max_string_length do nothing
        if (
            max_len_string_array(ensure_object(encoded._values))
            <= self._max_string_length
        ):
            self.data[col] = encoded
