# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
exit(self.call_with_variable_creator_scope(self._fn)(*args, **kwargs))
