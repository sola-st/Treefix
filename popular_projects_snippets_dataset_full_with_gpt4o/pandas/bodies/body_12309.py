# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
str_lens = (1, 100, 244)
s = {}
for str_len in str_lens:
    s["s" + str(str_len)] = Series(
        ["a" * str_len, "b" * str_len, "c" * str_len]
    )
original = DataFrame(s)
with tm.ensure_clean() as path:
    original.to_stata(path, write_index=False)

    with StataReader(path) as sr:
        typlist = sr.typlist
        variables = sr.varlist
        formats = sr.fmtlist
        for variable, fmt, typ in zip(variables, formats, typlist):
            assert int(variable[1:]) == int(fmt[1:-1])
            assert int(variable[1:]) == typ
