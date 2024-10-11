# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring.py
"""Calls decorated function object.

    Also verifies if the function is compatible with TFLite.

    Returns:
      A execution result of the decorated function.
    """

if not self._verified:
    model = self._get_func()
    concrete_func = model.get_concrete_function(*args, **kwargs)
    converter = lite.TFLiteConverterV2.from_concrete_functions(
        [concrete_func], model)
    # Set provided converter parameters
    if self._converter_target_spec is not None:
        converter.target_spec = self._converter_target_spec
    if self._converter_allow_custom_ops is not None:
        converter.allow_custom_ops = self._converter_allow_custom_ops
    try:
        converter.convert()
    except convert.ConverterError as err:
        self._decode_error(err)
    finally:
        self._verified = True

exit(self._get_func()(*args, **kwargs))
