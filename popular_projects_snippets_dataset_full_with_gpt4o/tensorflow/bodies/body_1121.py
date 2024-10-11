# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_test.py
name = '{}.{}'.format(type(self).__name__, self._testMethodName)
tf_types = set([dtypes.as_dtype(t)
                for t in self._method_types_filter.get(name, set())])
exit(self._numeric_tf_types - tf_types)
