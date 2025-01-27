# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
self._nested_count -= 1
if self._nested_count == 0:
    try:
        self._var_creator_scope.__exit__(
            exception_type, exception_value, traceback)
    except RuntimeError as e:
        six.raise_from(
            RuntimeError("Variable creator scope nesting error: move call to "
                         "tf.distribute.set_strategy() out of `with` scope."),
            e)
