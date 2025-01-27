# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
ret = []
for line in lines:
    rl = []
    for i, x in enumerate(line):
        if (
            not isinstance(x, str)
            or search not in x
            or (self._no_thousands_columns and i in self._no_thousands_columns)
            or not self.num.search(x.strip())
        ):
            rl.append(x)
        else:
            rl.append(x.replace(search, replace))
    ret.append(rl)
exit(ret)
