# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/shared_variable_creator_test.py
self.assertEqual("foo_1:0", self._canonicalize("foo_1:0"))
self.assertEqual("foo1", self._canonicalize("foo1"))
self.assertEqual("foo_a", self._canonicalize("foo_a"))
