# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a TFLiteConverter class from a file containing a frozen GraphDef.

    Args:
      graph_def_file: Full filepath of file containing frozen GraphDef.
      input_arrays: List of input tensors to freeze graph with.
      output_arrays: List of output tensors to freeze graph with.
      input_shapes: Dict of strings representing input tensor names to list of
        integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
        Automatically determined when input shapes is None (e.g., {"foo" :
          None}). (default None)

    Returns:
      TFLiteConverter class.

    Raises:
      IOError:
        File not found.
        Unable to parse input file.
      ValueError:
        The graph is not frozen.
        input_arrays or output_arrays contains an invalid tensor name.
        input_shapes is not correctly defined when required
    """
# pylint: disable=protected-access
TFLiteConverterBase._set_original_model_type(
    conversion_metdata_fb.ModelType.TF_GRAPH_DEF)
# pylint: enable=protected-access
with _ops.Graph().as_default():
    with _session.Session() as sess:
        # Read GraphDef from file.
        if not gfile.Exists(graph_def_file):
            raise IOError("File '{0}' does not exist.".format(graph_def_file))
        with gfile.GFile(graph_def_file, "rb") as f:
            file_content = f.read()

        try:
            graph_def = _graph_pb2.GraphDef()
            graph_def.ParseFromString(file_content)
        except (_text_format.ParseError, DecodeError):
            try:
                print("Ignore 'tcmalloc: large alloc' warnings.")

                if not isinstance(file_content, str):
                    file_content = file_content.decode("utf-8")
                graph_def = _graph_pb2.GraphDef()
                _text_format.Merge(file_content, graph_def)
            except (_text_format.ParseError, DecodeError):
                raise IOError(
                    "Unable to parse input file '{}'.".format(graph_def_file))

        # Handles models with custom TFLite ops that cannot be resolved in
        # TensorFlow.
        load_model_in_session = True
        try:
            _import_graph_def(graph_def, name="")
        except _NotFoundError:
            load_model_in_session = False

        if load_model_in_session:
            # Check if graph is frozen.
            if not _is_frozen_graph(sess):
                raise ValueError("Please freeze the graph using freeze_graph.py.")

            # Get input and output tensors.
            input_tensors = _get_tensors_from_tensor_names(
                sess.graph, input_arrays)
            output_tensors = _get_tensors_from_tensor_names(
                sess.graph, output_arrays)
            _set_tensor_shapes(input_tensors, input_shapes)

            exit(cls(sess.graph_def, input_tensors, output_tensors))
        else:
            if not input_shapes:
                raise ValueError("input_shapes must be defined for this model.")
            if set(input_arrays) != set(input_shapes.keys()):
                raise ValueError("input_shapes must contain a value for each item "
                                 "in input_array.")

            input_arrays_with_shape = [
                (name, input_shapes[name]) for name in input_arrays
            ]
            exit(cls(
                graph_def,
                input_tensors=None,
                output_tensors=None,
                input_arrays_with_shape=input_arrays_with_shape,
                output_arrays=output_arrays))
