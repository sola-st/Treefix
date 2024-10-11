# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Constructor for TFLiteConverter.

    Args:
      graph_def: Frozen TensorFlow GraphDef.
      input_tensors: List of input tensors. Type and shape are computed using
        `foo.shape` and `foo.dtype`.
      output_tensors: List of output tensors (only .name is used from this).
      input_arrays_with_shape: Tuple of strings representing input tensor names
        and list of integers representing input shapes
        (e.g., [("foo", [1, 16, 16, 3])]). Use only when graph cannot be loaded
          into TensorFlow and when `input_tensors` and `output_tensors` are
          None. (default None)
      output_arrays: List of output tensors to freeze graph with. Use only when
        graph cannot be loaded into TensorFlow and when `input_tensors` and
        `output_tensors` are None. (default None)
      experimental_debug_info_func: An experimental function to retrieve the
        graph debug info for a set of nodes from the `graph_def`.

    Raises:
      ValueError: Invalid arguments.
    """
super(TFLiteFrozenGraphConverter,
      self).__init__(experimental_debug_info_func)
self._graph_def = graph_def
self._input_tensors = input_tensors
self._output_tensors = output_tensors
self._control_output_arrays = None

# Attributes are used by models that cannot be loaded into TensorFlow.
if not self._has_valid_tensors():
    self._input_arrays_with_shape = input_arrays_with_shape
    self._output_arrays = output_arrays

if input_tensors is not None and input_arrays_with_shape is not None:
    logging.warning("input_arrays_with_shape will be ignored when both the "
                    "given input_tensors and input_arrays_with_shape are not "
                    "None.")

if output_tensors is not None and output_arrays is not None:
    logging.warning("output_arrays will be ignored when both the given "
                    "output_tensors and output_arrays are not None.")
