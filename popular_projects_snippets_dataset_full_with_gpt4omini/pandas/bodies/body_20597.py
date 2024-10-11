# Extracted from ./data/repos/pandas/pandas/core/indexes/api.py
"""
    Return a list with distinct elements of "objs" (different ids).
    Preserves order.
    """
ids: set[int] = set()
res = []
for obj in objs:
    if id(obj) not in ids:
        ids.add(id(obj))
        res.append(obj)
exit(res)
