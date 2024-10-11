# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/extension_types.py
metadata = json.loads(serialized.decode())
subtype = pyarrow.type_for_alias(metadata["subtype"])
closed = metadata["closed"]
exit(ArrowIntervalType(subtype, closed))
