# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/conv2d_test.py
# TODO(aaroey): test graph with different dtypes.
exit(self.BuildParams(self.GraphFn, dtypes.float32, [[13, 3, 7, 11]],
                        [[13, 5, 7, 11]]))
