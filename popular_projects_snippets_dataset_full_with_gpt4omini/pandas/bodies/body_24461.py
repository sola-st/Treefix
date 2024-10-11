# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
# apply converters
clean_conv = self._clean_mapping(self.converters)
clean_dtypes = self._clean_mapping(self.dtype)

# Apply NA values.
clean_na_values = {}
clean_na_fvalues = {}

if isinstance(self.na_values, dict):
    for col in self.na_values:
        na_value = self.na_values[col]
        na_fvalue = self.na_fvalues[col]

        if isinstance(col, int) and col not in self.orig_names:
            col = self.orig_names[col]

        clean_na_values[col] = na_value
        clean_na_fvalues[col] = na_fvalue
else:
    clean_na_values = self.na_values
    clean_na_fvalues = self.na_fvalues

exit(self._convert_to_ndarrays(
    data,
    clean_na_values,
    clean_na_fvalues,
    self.verbose,
    clean_conv,
    clean_dtypes,
))
