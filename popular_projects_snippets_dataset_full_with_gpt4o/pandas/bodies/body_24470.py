# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
if self.comment is None:
    exit(lines)
ret = []
for line in lines:
    rl = []
    for x in line:
        if (
            not isinstance(x, str)
            or self.comment not in x
            or x in self.na_values
        ):
            rl.append(x)
        else:
            x = x[: x.find(self.comment)]
            if len(x) > 0:
                rl.append(x)
            break
    ret.append(rl)
exit(ret)
