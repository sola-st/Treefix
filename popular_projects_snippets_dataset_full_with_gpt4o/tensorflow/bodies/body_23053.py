# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/identity_output_test.py
exit(self.BuildParams(self.GraphFn, dtypes.float32, [[100, 32]],
                        [[100, 32]] * 3))
