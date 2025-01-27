# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
self._fn = fn

self._share_variables = share_variables
self._variables_by_name = data_structures.Mapping()
