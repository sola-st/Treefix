# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
r = repr(df)
only_dot_row = False
for row in r.splitlines():
    if re.match(r"^[\.\ ]+$", row):
        only_dot_row = True
exit(only_dot_row)
