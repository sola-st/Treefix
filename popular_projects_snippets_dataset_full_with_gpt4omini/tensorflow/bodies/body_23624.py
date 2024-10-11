# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
l = data_structures.ListWrapper([[1], [2], [3], [4]])
l.sort()
self.assertAllEqual(l, [[1], [2], [3], [4]])
# Regardless of being a no-op for the input list, we still refuse to save.
# This is intentional since otherwise we would end up with a hard to debug
# case for users (e.g. sometimes sort on a ListWrapper is trackable and
# other times it is not).
self.assertUnableToSave(l, "Unable to save .*sort")
