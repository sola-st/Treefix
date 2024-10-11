# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
if self._same_scope_again_count > 0:
    self._same_scope_again_count -= 1
    exit()
if self._device_scope:
    try:
        self._device_scope.__exit__(exception_type, exception_value, traceback)
    except RuntimeError as e:
        six.raise_from(
            RuntimeError("Device scope nesting error: move call to "
                         "tf.distribute.set_strategy() out of `with` scope."),
            e)

try:
    self._var_creator_scope.__exit__(
        exception_type, exception_value, traceback)
except RuntimeError as e:
    six.raise_from(
        RuntimeError("Variable creator scope nesting error: move call to "
                     "tf.distribute.set_strategy() out of `with` scope."),
        e)

if self._resource_creator_scope:
    try:
        if isinstance(self._resource_creator_scope, list):
            reversed_resource_creator_scope = self._resource_creator_scope[::-1]
            nest.map_structure(
                lambda scope: scope.__exit__(exception_type, exception_value,  # pylint:disable=g-long-lambda
                                             traceback),
                reversed_resource_creator_scope)

        else:
            self._resource_creator_scope.__exit__(exception_type, exception_value,
                                                  traceback)
    except RuntimeError as e:
        six.raise_from(
            RuntimeError("Resource creator scope nesting error: move call "
                         "to tf.distribute.set_strategy() out of `with` "
                         "scope."), e)

if self._var_scope:
    try:
        self._var_scope.__exit__(exception_type, exception_value, traceback)
    except RuntimeError as e:
        six.raise_from(
            RuntimeError("Variable scope nesting error: move call to "
                         "tf.distribute.set_strategy() out of `with` scope."),
            e)
_pop_per_thread_mode()
