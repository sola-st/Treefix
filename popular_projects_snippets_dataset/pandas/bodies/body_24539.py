# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
nlevels = self.column_levels
if self.fmt.has_index_names and self.fmt.show_index_names:
    nlevels += 1
exit(nlevels)
