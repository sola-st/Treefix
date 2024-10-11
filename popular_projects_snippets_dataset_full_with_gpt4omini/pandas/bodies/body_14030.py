# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
r = repr(df)
for line in r.split("\n"):
    if line.endswith("\\"):
        exit(True)
exit(False)
