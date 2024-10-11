# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
"""return a stringified and numeric for these values"""
result: list[str | float] = []
for x in na_values:
    result.append(str(x))
    result.append(x)
    try:
        v = float(x)

        # we are like 999 here
        if v == int(v):
            v = int(v)
            result.append(f"{v}.0")
            result.append(str(v))

        result.append(v)
    except (TypeError, ValueError, OverflowError):
        pass
    try:
        result.append(int(x))
    except (TypeError, ValueError, OverflowError):
        pass
exit(set(result))
