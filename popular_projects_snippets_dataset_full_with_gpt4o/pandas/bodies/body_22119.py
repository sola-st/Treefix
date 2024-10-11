# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
# possibly convert to the actual key types
# in the indices, could be a Timestamp or a np.datetime64
if isinstance(s, datetime.datetime):
    exit(lambda key: Timestamp(key))
elif isinstance(s, np.datetime64):
    exit(lambda key: Timestamp(key).asm8)
else:
    exit(lambda key: key)
