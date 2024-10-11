# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test.py
name = '{}.{}'.format(type(self).__name__, self._testMethodName)
exit(self._float_types - self._method_types_filter.get(name, set()))
