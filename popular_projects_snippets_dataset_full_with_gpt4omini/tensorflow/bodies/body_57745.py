# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring.py
"""Initialize the decorator object.

    Here is the description of the object variables.
    - _func     : decorated function.
    - _obj_func : for class object, we need to use this object to provide `self`
                  instance as 1 first argument.
    - _verified : whether the compatibility is checked or not.

    Args:
      target: decorated function.
      converter_target_spec : target_spec of TFLite converter parameter.
      converter_allow_custom_ops : allow_custom_ops of TFLite converter
          parameter.
      raise_exception : to raise an exception on compatibility issues.
          User need to use get_compatibility_log() to check details.
    """
functools.update_wrapper(self, target)
self._func = target
self._obj_func = None
self._verified = False
self._log_messages = []
self._raise_exception = raise_exception
self._converter_target_spec = converter_target_spec
self._converter_allow_custom_ops = converter_allow_custom_ops
