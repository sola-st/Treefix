# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
mapping = data_structures.Mapping()
original = data_structures.List()
mapping["a"] = original
with self.assertRaises(ValueError):
    mapping["a"] = data_structures.List()
self.assertIs(original, mapping["a"])
with self.assertRaises(AttributeError):
    del mapping["a"]  # pylint: disable=unsupported-delete-operation
mapping.update(b=data_structures.Mapping())
with self.assertRaises(ValueError):
    mapping.update({"b": data_structures.Mapping()})
