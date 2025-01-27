# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/bool_test.py
shape = [2, 32, 32, 3]
exit(self.BuildParams(self.GraphFn, dtypes.bool, [shape, shape], [shape]))
