# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Constructor for TFLiteConverter.

    Args:
      model_file: Full filepath of HDF5 file containing the tf.keras model.
      input_arrays: List of input tensors to freeze graph with. Uses input
        arrays from SignatureDef when none are provided. (default None)
      input_shapes: Dict of strings representing input tensor names to list of
        integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
        Automatically determined when input shapes is None (e.g., {"foo" :
          None}). (default None)
      output_arrays: List of output tensors to freeze graph with. Uses output
        arrays from SignatureDef when none are provided. (default None)
      custom_objects: Dict mapping names (strings) to custom classes or
        functions to be considered during model deserialization. (default None)

    Raises:
      ValueError: Invalid arguments.
    """
super(TFLiteKerasModelConverter,
      self).__init__(experimental_debug_info_func=None)
# Handles Keras when Eager mode is enabled.
if context.executing_eagerly():
    if input_arrays or output_arrays:
        raise ValueError("`input_arrays` and `output_arrays` are unsupported "
                         "with Eager mode. If your model requires any of these "
                         "parameters, please use disable_eager_execution().")

    keras_model = keras_deps.get_load_model_function()(model_file,
                                                       custom_objects)
    function = _trace_model_call(keras_model)
    concrete_func = function.get_concrete_function()

    frozen_func = _convert_to_constants.convert_variables_to_constants_v2(
        concrete_func, lower_control_flow=False)
    _set_tensor_shapes(frozen_func.inputs, input_shapes)
    self._keras_model = keras_model
    self._graph_def = frozen_func.graph.as_graph_def()
    self._input_tensors = frozen_func.inputs
    self._output_tensors = frozen_func.outputs
    self._debug_info_func = _build_debug_info_func(frozen_func.graph)
    exit()

# Handles Keras when Eager mode is disabled.
keras_deps.get_clear_session_function()()
keras_model = keras_deps.get_load_model_function()(model_file,
                                                   custom_objects)
sess = keras_deps.get_get_session_function()()

# Get input and output tensors.
if input_arrays:
    input_tensors = _get_tensors_from_tensor_names(sess.graph, input_arrays)
else:
    input_tensors = keras_model.inputs

if output_arrays:
    output_tensors = _get_tensors_from_tensor_names(sess.graph, output_arrays)
else:
    output_tensors = keras_model.outputs
_set_tensor_shapes(input_tensors, input_shapes)

graph_def = _freeze_graph(sess, input_tensors, output_tensors)
self._keras_model = keras_model
self._graph_def = graph_def
self._input_tensors = input_tensors
self._output_tensors = output_tensors
self._debug_info_func = _build_debug_info_func(sess.graph)
