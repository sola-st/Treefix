# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/batch_matmul_test.py
exit(self.BuildParams(self.GraphFn, dtypes.float32,
                        [[12, 5, 8, 12], [12, 5, 12, 7]], [[12, 5, 8, 7]]))
