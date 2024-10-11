# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_mode_test.py
"""We specify input/output masks with static (known) shapes."""
exit(self.BuildParamsWithMask(
    self.GraphFn,
    dtypes.float32, [[1, 12, 5]], [[12, 5]],
    input_mask=[[True, True, True]],
    output_mask=[[True, True]],
    extra_inputs=[],
    extra_outputs=[]))
