# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
exit(self.BuildParamsWithMask(
    self.GraphFn,
    dtypes.float32, [[2, 2, 5, 3]], [[4]],
    extra_inputs=[[[8, 2, 5, 3]]],
    extra_outputs=[[[4]]],
    input_mask=[[False, True, True, True]],
    output_mask=[[True]]))
