# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
exit(self.BuildParamsWithMask(
    self.GraphFn,
    dtypes.float32, [[1, 2, 5, 3], [2, 15]], [[4], [1, 2, 5, 3]],
    extra_inputs=[],
    extra_outputs=[],
    input_mask=[[False, True, True, True], [False, True]],
    output_mask=[[True], [False, True, True, True]]))
