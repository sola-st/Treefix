# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
exit(self.BuildParamsWithMask(
    self.GraphFn,
    dtypes.float32, [[2, 2, 5, 3]], [[4]],
    extra_inputs=[],
    extra_outputs=[],
    input_mask=[[False, True, True, True]],
    output_mask=[[True]]))
