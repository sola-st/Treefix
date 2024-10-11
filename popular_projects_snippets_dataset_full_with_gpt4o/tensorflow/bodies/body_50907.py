# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
func = super(RestoredFunction, self)._compiler_with_scope(scope)
func._function_spec = self._function_spec  # pylint: disable=protected-access
exit(func)
