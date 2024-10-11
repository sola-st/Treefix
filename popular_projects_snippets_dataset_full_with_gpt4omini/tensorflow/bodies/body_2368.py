# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/data_format_ops_test.py
self._test(0, "NHWC", "NCHW", 0)
self._test(1, "NHWC", "NCHW", 2)
self._test(2, "NHWC", "NCHW", 3)
self._test(3, "NHWC", "NCHW", 1)
self._test(-1, "NHWC", "NCHW", 1)
self._test(-2, "NHWC", "NCHW", 3)
self._test(-3, "NHWC", "NCHW", 2)
self._test(-4, "NHWC", "NCHW", 0)
self._test([1, 3], "NHWC", "NCHW", [2, 1])
self._test([1, 3, -2], "NHWC", "NCHW", [2, 1, 3])
self._test([1, -3, -2], "NHWC", "NCHW", [2, 2, 3])
self._test([[1, -3], [1, -1]], "NHWC", "NCHW", [[2, 2], [2, 1]])

self._test([1, -3, -2], "NHWC", "NCHW", [2, 2, 3])
self._test([-4, -3, -2, -1, 0, 1, 2, 3], "NHWC", "HWNC",
           [2, 0, 1, 3, 2, 0, 1, 3])
self._test([-4, -3, -2, -1, 0, 1, 2, 3], "NHWC", "WHCN",
           [3, 1, 0, 2, 3, 1, 0, 2])
self._test([-4, -3, -2, -1, 0, 1, 2, 3], "qwer", "rewq",
           [3, 2, 1, 0, 3, 2, 1, 0])

self._test(0, "NDHWC", "NCDHW", 0)
self._test(1, "NDHWC", "NCDHW", 2)
self._test(2, "NDHWC", "NCDHW", 3)
self._test(3, "NDHWC", "NCDHW", 4)
self._test(4, "NDHWC", "NCDHW", 1)
self._test([1, 4], "NDHWC", "NCDHW", [2, 1])
self._test([1, 4, -2], "NDHWC", "NCDHW", [2, 1, 4])
self._test([1, -3, -2], "NDHWC", "NCDHW", [2, 3, 4])
self._test([[1, -4], [1, -1]], "NDHWC", "NCDHW", [[2, 2], [2, 1]])

self._test([1, -3, -2], "NDHWC", "NCDHW", [2, 3, 4])
self._test([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], "NDHWC", "DHWNC",
           [3, 0, 1, 2, 4, 3, 0, 1, 2, 4])
self._test([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4], "NDHWC", "WHDCN",
           [4, 2, 1, 0, 3, 4, 2, 1, 0, 3])
