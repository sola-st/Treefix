# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/batch_matmul_test.py
exit(self.BuildParamsWithMask(
    graph_fn=graph_fn,
    dtype=dtype,
    input_shapes=input_shapes,
    output_shapes=output_shapes,
    input_mask=[[True] * len(s) for s in input_shapes],
    output_mask=[[True] * len(s) for s in output_shapes],
    extra_inputs=[],
    extra_outputs=[]))
