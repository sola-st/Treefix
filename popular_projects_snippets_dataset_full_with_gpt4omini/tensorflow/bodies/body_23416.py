# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
if y <= 0:
    raise ValueError(
        f"List only supports append, multiplying in place by {y} removes "
        "elements.")

n = len(self._storage)
for _ in range(y - 1):
    for i in range(n):
        self.append(self._storage[i])

exit(self)
