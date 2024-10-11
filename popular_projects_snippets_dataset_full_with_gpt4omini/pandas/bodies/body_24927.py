# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
exit(format_array(
    self.tr_series._values,
    None,
    float_format=self.float_format,
    na_rep=self.na_rep,
    leading_space=self.index,
))
