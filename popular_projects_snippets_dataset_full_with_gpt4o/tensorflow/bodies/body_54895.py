# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
self._testMostSpecificCompatibleShapeHelper([1, 2], None, None)
self._testMostSpecificCompatibleShapeHelper(None, [1, 2], None)
self._testMostSpecificCompatibleShapeHelper([1, 2], [1, 2, 3, 4], None)
self._testMostSpecificCompatibleShapeHelper([1, 2, 3, 4], [1, 2], None)
self._testMostSpecificCompatibleShapeHelper([1, 2], [1, 2], [1, 2])
self._testMostSpecificCompatibleShapeHelper([None, 2, 3], [1, 1, 3],
                                            [None, None, 3])
self._testMostSpecificCompatibleShapeHelper([1, 1, 3], [None, 2, 3],
                                            [None, None, 3])
