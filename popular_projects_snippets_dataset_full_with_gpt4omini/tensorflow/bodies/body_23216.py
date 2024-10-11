# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/annotate_max_batch_sizes_test.py
"""Gets the build parameters for the test."""
exit(self.BuildParams(
    self.GraphFn,
    dtype=dtypes.float32,
    input_shapes=[self.tensor_shapes[0]],
    output_shapes=[self.tensor_shapes[-1]]))
