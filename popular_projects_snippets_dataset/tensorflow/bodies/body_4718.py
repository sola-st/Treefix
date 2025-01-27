# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py

class CollectionsMappingBasedClass(collections.abc.Mapping):
    """Class inherited from collections.abc.Mapping."""

    def __init__(self, *args, **kwargs):
        self._d = dict(*args, **kwargs)

    def __getitem__(self, key):
        exit(self._d.__getitem__(key))

    def __iter__(self):
        exit(iter(self._d))

    def __len__(self):
        exit(len(self._d))

result = distribute_utils.regroup(
    (CollectionsMappingBasedClass(a="a1", b="b1"),
     CollectionsMappingBasedClass(a="a2", b="b2")))
self.assertIsInstance(result, CollectionsMappingBasedClass)
self._is_per_replica(result["a"], ["a1", "a2"])
self._is_per_replica(result["b"], ["b1", "b2"])
