# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
for shape_ in shapes:
    for dtype_ in dtypes:
        for batch_ in False, True:
            self._runOneTest(shape_, dtype_, batch_, scalar_test)
