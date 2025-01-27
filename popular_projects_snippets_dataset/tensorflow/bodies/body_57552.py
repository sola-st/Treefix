# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a TFLiteConverter object from ConcreteFunctions.

    Args:
      funcs: List of TensorFlow ConcreteFunctions. The list should not contain
        duplicate elements. Currently converter can only convert a single
        ConcreteFunction. Converting multiple functions is under development.
      trackable_obj:   An `AutoTrackable` object (typically `tf.module`)
        associated with `funcs`. A reference to this object needs to be
        maintained so that Variables do not get garbage collected since
        functions have a weak reference to Variables.

    Returns:
      TFLiteConverter object.

    Raises:
      Invalid input type.
    """
# pylint: disable=protected-access
TFLiteConverterBase._set_original_model_type(
    conversion_metdata_fb.ModelType.TF_CONCRETE_FUNCTIONS)
# pylint: enable=protected-access
if trackable_obj is None:
    logging.warning(
        "Please consider providing the trackable_obj argument in the "
        "from_concrete_functions. Providing without the trackable_obj "
        "argument is deprecated and it will use the deprecated conversion "
        "path.")
for func in funcs:
    if not isinstance(func, _function.ConcreteFunction):
        message = "This function takes in a list of ConcreteFunction."
        if isinstance(func, _def_function.Function):
            message += (" To get the ConcreteFunction from a Function,"
                        " call get_concrete_function.")
        raise ValueError(message)
exit(cls(funcs, trackable_obj))
