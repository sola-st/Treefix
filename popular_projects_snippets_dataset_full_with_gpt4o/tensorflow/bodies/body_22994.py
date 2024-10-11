# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
# TODO(aaroey): test graph with different dtypes.
exit(self.BuildParams(self.GraphFn, dtypes.float32, [[100, 24, 24, 2]],
                        [[100, 6, 6, 6]]))
