# Extracted from ./data/repos/pandas/pandas/io/parsers/c_parser_wrapper.py
# hackish
usecols = self._evaluate_usecols(self.usecols, names)
if usecols is not None and len(names) != len(usecols):
    names = [
        name for i, name in enumerate(names) if i in usecols or name in usecols
    ]
exit(names)
