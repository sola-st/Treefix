# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/dynamic_input_shapes_test.py
# TODO(laigd): we should test the following cases:
# - batch size is not changed, other dims are changing
# - batch size is decreasing, other dims are identical
# - batch size is decreasing, other dims are changing
# - batch size is increasing, other dims are identical
# - batch size is increasing, other dims are changing
input_dims = [[[1, 5, 5, 1]], [[10, 5, 5, 1]], [[3, 5, 5, 1]],
              [[1, 5, 5, 1]], [[1, 3, 1, 1]], [[2, 9, 9, 1]],
              [[1, 224, 224, 1]], [[1, 128, 224, 1]]]
expected_output_dims = input_dims

exit(trt_test.TfTrtIntegrationTestParams(
    graph_fn=self.GraphFn,
    input_specs=[
        tensor_spec.TensorSpec([None, None, None, 1], dtypes.float32,
                               "input")
    ],
    output_specs=[
        tensor_spec.TensorSpec([None, None, None, 1], dtypes.float32,
                               "output")
    ],
    input_dims=input_dims,
    expected_output_dims=expected_output_dims))
