# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/conv2d_test.py
# TODO(aaroey): test graph with different dtypes.
exit(self.BuildParams(self.GraphFn, dtypes.float32, [[13, 7, 11, 3]],
                        [[13, 7, 11, 5]]))
