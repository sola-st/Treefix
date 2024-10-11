# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Build test parameters.

    The input_shapes and output_shapes arguments are known (static) shapes that
    can be used to generate test data. To define the model, we also specify
    corresponding input/output TensorSpecs. These are defined using the shape
    arguments. For each input tensor we define:

    input_spec = [None] + input_shape[1:]

    and similarly for output shapes. This means that we leave the first (batch)
    dimension unknown, the rest is just copied from the shapes arg.

    Args:
      graph_fn: The function to build the graph.
      dtype: The element type.
      input_shapes: The input shapes.
      output_shapes: The output shapes.

    Returns:
      The test parameters.
    """

input_mask = [[False] + [True] * (len(shape) - 1) for shape in input_shapes]
output_mask = [[False] + [True] * (len(shape) - 1) if shape else []
               for shape in output_shapes]

exit(self.BuildParamsWithMask(graph_fn, dtype, input_shapes,
                                output_shapes, input_mask, output_mask, [],
                                []))
