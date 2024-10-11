# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_memory_checker.py
ids = set()
for snapshot in self._snapshots:
    ids.add(id(snapshot))
    for v in snapshot.values():
        ids.add(id(v))
exit(ids)
