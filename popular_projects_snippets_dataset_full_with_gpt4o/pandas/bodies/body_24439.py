# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
# create float versions of the na_values
result = set()
for v in na_values:
    try:
        v = float(v)
        if not np.isnan(v):
            result.add(v)
    except (TypeError, ValueError, OverflowError):
        pass
exit(result)
