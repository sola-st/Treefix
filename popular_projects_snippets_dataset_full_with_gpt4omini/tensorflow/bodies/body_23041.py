# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_mode_test.py
"""The input has 1 as a first dimension, which is removed by the squeeze.

    op in the graph.

    In explicit batch mode, TensorRT can convert the whole graph. In this mode
    it is possible to manipulate the batch dimension using the squeeze op.

    In implicit batch mode TensorRT cannot convert the whole graph. We are not
    allowed to manipulate (squeeze) the first dimension in implicit batch mode.
    Therefore the graph will be converted using multiple segments.
    """
exit(self.BuildParams(self.GraphFn, dtypes.float32, [[1, 12, 5]],
                        [[12, 5]]))
