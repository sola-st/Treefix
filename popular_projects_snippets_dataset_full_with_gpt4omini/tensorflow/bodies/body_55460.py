# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
with self.assertRaises(InvalidArgumentError) as cm:
    self._testNestedDeviceWithSameFunction("MatmulTest")
self.assertEqual(
    cm.exception.message,
    "Cannot add function \'MatmulTest\' because a different "
    "function with the same name already exists.")
