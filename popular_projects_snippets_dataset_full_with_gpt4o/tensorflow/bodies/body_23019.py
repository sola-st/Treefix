# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/rank_two_test.py
exit(self.BuildParams(self.GraphFn, dtypes.float32,
                        [[12, 5], [12, 5, 2, 2]], [[12, 5, 2, 2]]))
