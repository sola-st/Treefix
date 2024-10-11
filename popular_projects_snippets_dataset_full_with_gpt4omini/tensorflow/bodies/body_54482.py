# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
super(_TupleTensor, self).__init__()
self._components = tuple(ops.convert_to_tensor(c) for c in components)
