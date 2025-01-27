# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/shape_output_test.py
exit(self.BuildParamsWithMask(
    self.GraphFn,
    dtypes.float16, [[3], []], [[3]],
    extra_inputs=[],
    extra_outputs=[],
    input_mask=[[True], []],
    output_mask=[[True]]))
