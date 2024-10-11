# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
if count != 1:
    assert count == int(count)
    count = int(count)
    exit(f"{count}{base}")
else:
    exit(base)
