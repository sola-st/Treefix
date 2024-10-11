# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
value = [0, 1, 2, 3, 4, 5]

for shape in [[2, 4], [2, 2]]:
    self._testNDimConstantInitializerIncorrectNumberValues(value, shape)
    self._testNDimConstantInitializerIncorrectNumberValues(
        np.asarray(value), shape)
    self._testNDimConstantInitializerIncorrectNumberValues(
        np.asarray(value).reshape(tuple([2, 3])), shape)
