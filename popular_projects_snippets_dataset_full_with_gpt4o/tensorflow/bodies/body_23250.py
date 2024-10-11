# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/topk_test.py
k = 5
exit(self.BuildParams(self.GraphFn, dtypes.float32, [[100, 100]],
                        [[100, k], [100, k]]))
