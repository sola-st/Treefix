# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session():
    self.assertAllEqual((None, None), self._get_test_attrs())
