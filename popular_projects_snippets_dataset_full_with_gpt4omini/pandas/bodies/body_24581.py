# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
self.fmt = formatter
self.frame = self.fmt.frame
self.longtable = longtable
self.column_format = column_format
self.multicolumn = multicolumn
self.multicolumn_format = multicolumn_format
self.multirow = multirow
self.caption, self.short_caption = _split_into_full_short_caption(caption)
self.label = label
self.position = position
