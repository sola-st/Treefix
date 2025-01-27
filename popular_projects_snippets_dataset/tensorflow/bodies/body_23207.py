# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/unary_test.py
exit(self.BuildParams(self.GraphFn, dtypes.float32,
                        [[12, 5, 8, 1, 1, 12], [12, 5, 8, 1, 12, 1, 1]],
                        [[12, 5, 8, 12]]))
