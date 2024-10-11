# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
if formatters is None:
    exit({})
elif len(self.frame.columns) == len(formatters) or isinstance(formatters, dict):
    exit(formatters)
else:
    raise ValueError(
        f"Formatters length({len(formatters)}) should match "
        f"DataFrame number of columns({len(self.frame.columns)})"
    )
