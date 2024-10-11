# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
iterator = self._create_row_iterator(over="header")
exit("\n".join(list(iterator)))
