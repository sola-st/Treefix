# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_mode_test.py
"""We specify input/output mask with dynamic (unknown) shapes.

    In dynamic shape mode, single engine with three optimization profiles can
    handle the three different input shapes.
    """
exit(self.BuildParamsWithMask(
    self.GraphFn,
    dtypes.float32, [[1, 12, 5]], [[12, 5]],
    extra_inputs=[[[1, 2, 3]], [[1, 4, 6]]],
    extra_outputs=[[[2, 3]], [[4, 6]]],
    input_mask=[[False, False, False]],
    output_mask=[[False, False]]))
