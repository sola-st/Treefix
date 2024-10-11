# Extracted from ./data/repos/pandas/pandas/tests/window/moments/conftest.py
values = x.values.ravel("K")
exit(len(set(values[notna(values)])) == 1)
