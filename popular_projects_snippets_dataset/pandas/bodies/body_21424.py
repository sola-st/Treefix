# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/extension_types.py
metadata = json.loads(serialized.decode())
exit(ArrowPeriodType(metadata["freq"]))
