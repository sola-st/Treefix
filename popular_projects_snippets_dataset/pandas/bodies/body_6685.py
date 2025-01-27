# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_frozen.py
q = r = container

q += [5]
self.check_result(q, lst + [5])

# Other shouldn't be mutated.
self.check_result(r, lst)
