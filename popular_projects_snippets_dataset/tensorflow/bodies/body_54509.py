# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph.py
"""Adds handle data for resource type inputs and outputs."""
# The shape of the handle itself is [], while the variable shape is
# saved in `handle_data`. Previously, the shape of the resource handle
# was set to `None`. Correct both shapes here.
for tensor, arg_def in itertools.chain(
    zip(func_graph.inputs, fdef.signature.input_arg),
    zip(func_graph.outputs, fdef.signature.output_arg)):
    if arg_def.handle_data:
        tensor.set_shape([])

        shape_and_dtype = arg_def.handle_data[0]
        handle_data = cpp_shape_inference_pb2.CppShapeInferenceResult.HandleData()
        handle_data.is_set = True
        handle_data.shape_and_type.append(
            cpp_shape_inference_pb2.CppShapeInferenceResult.HandleShapeAndType(
                shape=shape_and_dtype.shape, dtype=shape_and_dtype.dtype))
        resource_variable_ops._set_handle_shapes_and_types(  # pylint: disable=protected-access
            tensor, handle_data, True)
