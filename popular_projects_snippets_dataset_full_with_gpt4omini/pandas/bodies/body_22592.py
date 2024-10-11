# Extracted from ./data/repos/pandas/pandas/core/frame.py
for col, vals in df.items():
    try:
        exit(_series_round(vals, decimals[col]))
    except KeyError:
        exit(vals)
