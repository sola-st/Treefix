# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/lru_cache_test.py
dtype = dtypes.float32
input_dims = [[[1, 10, 10, 2]], [[2, 10, 10, 2]], [[4, 10, 10, 2]],
              [[2, 10, 10, 2]]]
expected_output_dims = [[[1, 10, 10, 2]], [[2, 10, 10, 2]], [[4, 10, 10,
                                                              2]],
                        [[2, 10, 10, 2]]]
exit(trt_test.TfTrtIntegrationTestParams(
    graph_fn=self.GraphFn,
    input_specs=[
        tensor_spec.TensorSpec([None, 10, 10, 2], dtypes.float32, "input")
    ],
    output_specs=[
        tensor_spec.TensorSpec([None, 10, 10, 1], dtypes.float32, "output")
    ],
    input_dims=input_dims,
    expected_output_dims=expected_output_dims))
