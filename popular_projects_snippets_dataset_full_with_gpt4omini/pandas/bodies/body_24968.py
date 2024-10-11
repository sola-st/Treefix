# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
frame = self.tr_frame
formatter = self._get_formatter(i)
exit(format_array(
    frame.iloc[:, i]._values,
    formatter,
    float_format=self.float_format,
    na_rep=self.na_rep,
    space=self.col_space.get(frame.columns[i]),
    decimal=self.decimal,
    leading_space=self.index,
))
