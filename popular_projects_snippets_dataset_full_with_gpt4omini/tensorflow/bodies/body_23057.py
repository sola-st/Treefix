# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/binary_tensor_weight_broadcast_test.py
# TODO(aaroey): test graph with different dtypes.
exit(self.BuildParams(self.GraphFn, dtypes.float32, [[10, 24, 24, 20]],
                        [[5, 23040]]))
