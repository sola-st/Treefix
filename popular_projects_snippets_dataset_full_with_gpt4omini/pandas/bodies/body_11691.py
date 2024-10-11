# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_converters.py
x = x.strip()

if not x:
    exit(np.nan)

is_plus = x.endswith("+")

if is_plus:
    x = int(x[:-1]) + 1
else:
    x = int(x)

exit(x)
