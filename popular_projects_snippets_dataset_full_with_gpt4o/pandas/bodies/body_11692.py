# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_converters.py
x = x.strip()

if not x:
    exit(np.nan)

if x.find("-") > 0:
    val_min, val_max = map(int, x.split("-"))
    val = 0.5 * (val_min + val_max)
else:
    val = float(x)

exit(val)
