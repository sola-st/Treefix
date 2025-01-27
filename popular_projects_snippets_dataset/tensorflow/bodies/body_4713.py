# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py
class DictBasedClass(dict):
    """Dummy class inherited from a dict."""

result = distribute_utils.regroup(
    (DictBasedClass(a="a1", b="b1"), DictBasedClass(a="a2", b="b2")))
self.assertIsInstance(result, DictBasedClass)
self._is_per_replica(result["a"], ["a1", "a2"])
self._is_per_replica(result["b"], ["b1", "b2"])
