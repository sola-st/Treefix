# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
shapes = [[2, 32, 32, 3]]
exit(self.BuildParams(self.GraphFn, dtypes.float32, input_shapes=shapes,
                        output_shapes=shapes))
