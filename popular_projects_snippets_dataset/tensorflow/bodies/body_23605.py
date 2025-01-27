# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
not_overridden = []

for name in dir(list):
    if name in ListWrapperTest.IGNORED:
        continue

    list_method = getattr(list, name)

    if not callable(list_method):
        continue

    object_method = getattr(object, name, None)
    if object_method is not None and object_method == list_method:
        # Skip methods that aren't overridden from object.
        continue

    if list_method == getattr(data_structures.ListWrapper, name):
        not_overridden.append(name)

if not_overridden:
    self.fail("ListWrapper does not override %s" % (not_overridden))
