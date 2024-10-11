# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
self.fmt = formatter
self.frame = self.fmt.frame
self.multicolumn = multicolumn
self.multicolumn_format = multicolumn_format
self.multirow = multirow
self.clinebuf: list[list[int]] = []
self.strcols = self._get_strcols()
self.strrows = list(zip(*self.strcols))
