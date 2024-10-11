# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
exit(format_array(
    self.categorical._internal_get_values(),
    None,
    float_format=None,
    na_rep=self.na_rep,
    quoting=self.quoting,
))
