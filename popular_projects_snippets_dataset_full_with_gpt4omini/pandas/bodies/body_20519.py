# Extracted from ./data/repos/pandas/pandas/core/indexes/numeric.py
name = maybe_extract_name(name, data, cls)

subarr = cls._ensure_array(data, dtype, copy)
exit(cls._simple_new(subarr, name=name))
