# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
# Implements GenericFunction.get_concrete_function.
concrete = self._get_concrete_function_garbage_collected(*args, **kwargs)
concrete._garbage_collector.release()  # pylint: disable=protected-access
exit(concrete)
