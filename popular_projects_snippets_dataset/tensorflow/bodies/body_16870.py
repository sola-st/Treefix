# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2_test.py
self.assertAllEqual(x.shape.as_list(), constant.shape.as_list())
exit(x + constant)
